import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
import asyncio
import datetime
import os
import random
from pytz import timezone

from app.config import settings
from app.db import MemoryStore
from app.llm import LLMClient
from app.prompting import build_chat_messages, build_proactive_message_prompt, build_spontaneous_prompt, estimate_tokens

# 봇 설정
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=settings.bot_prefix, intents=intents)

# 사용자 시간대 설정 ( .env의 TIMEZONE 값 사용 )
USER_TZ = timezone(settings.timezone)

store = MemoryStore()
llm = LLMClient()
# 스케줄러에 설정된 시간대 적용
scheduler = AsyncIOScheduler(timezone=USER_TZ)

def get_current_time_str():
    """현재 설정된 시간대의 시간을 문자열로 반환"""
    return datetime.datetime.now(USER_TZ).strftime("%Y-%m-%d %H:%M:%S")

async def _broadcast_proactive(prompt_factory):
    cursor = store.conn.execute("SELECT user_id FROM sessions")
    users = cursor.fetchall()
    loop = asyncio.get_event_loop()
    for row in users:
        user_id = row["user_id"]
        try:
            user = await bot.fetch_user(int(user_id))
            if not user: continue
            rolling_summary = store.get_summary(user_id)
            now_str = get_current_time_str()
            prompt = prompt_factory(rolling_summary, now_str)
            
            # 푸시용 호출
            answer = await loop.run_in_executor(None, llm.chat, prompt)
            
            if settings.discord_channel_id > 0:
                channel = bot.get_channel(settings.discord_channel_id)
                if channel: await channel.send(f"<@{user_id}> {answer}")
            else:
                await user.send(answer)
            store.add_message(user_id, "assistant", f"[PUSH] {answer}", estimate_tokens(answer))
        except Exception as e:
            print(f"[PUSH_ERROR] {user_id}: {e}")

async def send_proactive_message(time_label: str):
    print(f"[*] Scheduled Job: {time_label}")
    await _broadcast_proactive(lambda summary, now: build_proactive_message_prompt(summary, time_label, now))

async def send_spontaneous_message():
    now = datetime.datetime.now(USER_TZ)
    if not (settings.spontaneous_start_hour <= now.hour <= settings.spontaneous_end_hour):
        return
    if random.random() > settings.spontaneous_chance:
        return
    print(f"[*] Spontaneous Message Decided!")
    await _broadcast_proactive(lambda summary, now_str: build_spontaneous_prompt(summary, now_str))

@bot.event
async def on_ready():
    print(f"[*] Logged in as: {bot.user.name}")
    print(f"[*] Active Persona: {settings.persona_name}")
    print(f"[*] System Timezone: {settings.timezone}")
    
    # 1. 정기 스케줄 등록
    for idx, t_str in enumerate(settings.schedule_times):
        label = settings.schedule_labels[idx] if idx < len(settings.schedule_labels) else f"Job {idx+1}"
        try:
            h, m = map(int, t_str.strip().split(":"))
            scheduler.add_job(
                send_proactive_message, 
                CronTrigger(hour=h, minute=m, timezone=USER_TZ), 
                args=[label.strip()]
            )
        except Exception as e:
            print(f"[!] Job Fail ({t_str}): {e}")
    
    # 2. 랜덤 돌발 스케줄 등록
    scheduler.add_job(send_spontaneous_message, IntervalTrigger(hours=settings.spontaneous_check_hours))
    
    if not scheduler.running:
        scheduler.start()
        print(f"[*] Scheduler Started (Fixed: {len(settings.schedule_times)}, Random: {settings.spontaneous_check_hours}h interval)")

@bot.command(name="초기화", aliases=["reset"])
async def reset_memory(ctx):
    """Resets the conversation memory for the user. / 대화 기록을 초기화합니다."""
    if settings.allowed_user_id and str(ctx.author.id) != settings.allowed_user_id: return
    user_id = str(ctx.author.id)
    store.update_summary(user_id, "")
    store.replace_with_compacted(user_id, [])
    await ctx.send(embed=discord.Embed(title="✨ System", description=settings.msg_reset_confirm, color=0x3498DB))

@bot.event
async def on_message(message):
    if message.author == bot.user: return
    if message.content.startswith(settings.bot_prefix):
        await bot.process_commands(message)
        return
    if settings.allowed_user_id and str(message.author.id) != settings.allowed_user_id: return

    user_id = str(message.author.id)
    utterance = message.content

    rolling_summary = store.get_summary(user_id)
    recent_messages = store.list_messages(user_id)[-settings.memory_keep_recent_messages:]

    store.ensure_session(user_id)
    store.add_message(user_id, "user", utterance, estimate_tokens(utterance))

    now_str = get_current_time_str()
    messages = build_chat_messages(rolling_summary, recent_messages, utterance, now_str)
    
    loop = asyncio.get_event_loop()
    async with message.channel.typing():
        answer = None
        for i in range(3):
            try:
                answer = await loop.run_in_executor(None, llm.chat, messages)
                if answer: break
            except Exception as e:
                print(f"[LLM_ERROR] Attempt {i+1}: {e}")
                if i < 2: await asyncio.sleep(1.5)

        if answer:
            await message.reply(answer)
            store.add_message(user_id, "assistant", answer, estimate_tokens(answer))
        else:
            await message.reply(settings.msg_llm_error)
    
    loop.run_in_executor(None, _compact_memory_if_needed_sync, user_id)

def _compact_memory_if_needed_sync(user_id: str):
    messages = store.list_messages(user_id)
    if sum(m["token_estimate"] for m in messages) <= settings.memory_token_budget: return
    keep_n = settings.memory_keep_recent_messages // 2
    to_keep, to_compress = messages[-keep_n:], messages[:-keep_n]
    if not to_compress: return
    chunk_text = "\n".join(f"[{m['role']}] {m['content']}" for m in to_compress)
    updated = llm.summarize(chunk_text, store.get_summary(user_id))
    store.update_summary(user_id, updated)
    store.replace_with_compacted(user_id, [m["id"] for m in to_keep])

if __name__ == "__main__":
    bot.run(settings.discord_token)
