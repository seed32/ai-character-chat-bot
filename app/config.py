import os
from dataclasses import dataclass, field
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

@dataclass
class Settings:
    # [LLM Settings]
    llm_provider: str = field(default_factory=lambda: os.getenv("LLM_PROVIDER", "gemini"))
    openai_api_key: str = field(default_factory=lambda: os.getenv("OPENAI_API_KEY", ""))
    gemini_api_key: str = field(default_factory=lambda: os.getenv("GEMINI_API_KEY", ""))
    gemini_api_keys: list[str] = field(default_factory=lambda: [
        os.getenv("GEMINI_API_KEY_1", ""), os.getenv("GEMINI_API_KEY_2", ""),
        os.getenv("GEMINI_API_KEY_3", ""), os.getenv("GEMINI_API_KEY_4", "")
    ])
    gemini_base_url: str = field(default_factory=lambda: os.getenv("GEMINI_BASE_URL", "https://generativelanguage.googleapis.com/v1beta/openai/"))

    llm_model_chat: str = field(default_factory=lambda: os.getenv("LLM_MODEL_CHAT", "gemini-1.5-flash"))
    llm_model_summary: str = field(default_factory=lambda: os.getenv("LLM_MODEL_SUMMARY", "gemini-1.5-flash"))
    llm_model_priority_1: str = field(default_factory=lambda: os.getenv("LLM_MODEL_PRIORITY_1", "gemini-1.5-flash"))
    llm_model_priority_2: str = field(default_factory=lambda: os.getenv("LLM_MODEL_PRIORITY_2", "gemini-1.5-flash-8b"))
    llm_model_priority_3: str = field(default_factory=lambda: os.getenv("LLM_MODEL_PRIORITY_3", "gemini-2.0-flash-lite-preview"))

    # [Persona Settings]
    persona_name: str = field(default_factory=lambda: os.getenv("PERSONA_NAME", "AI Character"))
    persona_profile: str = field(default_factory=lambda: os.getenv("PERSONA_PROFILE", "A friendly and helpful AI."))
    response_style: str = field(default_factory=lambda: os.getenv("RESPONSE_STYLE", "Casual and friendly."))
    emoji_policy: str = field(default_factory=lambda: os.getenv("EMOJI_POLICY", "Use emojis where appropriate."))
    persona_guardrails: str = field(default_factory=lambda: os.getenv("PERSONA_GUARDRAILS", "Never break character."))
    block_topics: str = field(default_factory=lambda: os.getenv("BLOCK_TOPICS", ""))
    sensitive_topics_rule: str = field(default_factory=lambda: os.getenv("SENSITIVE_TOPICS_RULE", "Redirect to experts if needed."))

    # Discord & Bot Settings
    discord_token: str = field(default_factory=lambda: os.getenv("DISCORD_TOKEN", ""))
    discord_channel_id: int = field(default_factory=lambda: int(os.getenv("DISCORD_CHANNEL_ID", "0")))
    bot_prefix: str = field(default_factory=lambda: os.getenv("BOT_PREFIX", "!"))
    allowed_user_id: str = field(default_factory=lambda: os.getenv("ALLOWED_USER_ID", ""))
    timezone: str = field(default_factory=lambda: os.getenv("TIMEZONE", "Asia/Seoul"))


    # [System Messages]
    msg_reset_confirm: str = field(default_factory=lambda: os.getenv("MSG_RESET_CONFIRM", "Memory has been reset."))
    msg_llm_error: str = field(default_factory=lambda: os.getenv("MSG_LLM_ERROR", "I'm having trouble thinking right now. Please try again later."))

    # [Scheduling Settings]
    schedule_times: list[str] = field(default_factory=lambda: os.getenv("SCHEDULE_TIMES", "09:00,12:00,18:00,23:00").split(","))
    schedule_labels: list[str] = field(default_factory=lambda: os.getenv("SCHEDULE_LABELS", "Morning,Lunch,Evening,Night").split(","))
    spontaneous_check_hours: int = field(default_factory=lambda: int(os.getenv("SPONTANEOUS_CHECK_HOURS", "1")))
    spontaneous_chance: float = field(default_factory=lambda: float(os.getenv("SPONTANEOUS_CHANCE", "0.1")))
    spontaneous_start_hour: int = field(default_factory=lambda: int(os.getenv("SPONTANEOUS_START_HOUR", "10")))
    spontaneous_end_hour: int = field(default_factory=lambda: int(os.getenv("SPONTANEOUS_END_HOUR", "22")))

    # [Memory Settings]
    memory_keep_recent_messages: int = field(default_factory=lambda: int(os.getenv("MEMORY_KEEP_RECENT_MESSAGES", "20")))
    memory_token_budget: int = field(default_factory=lambda: int(os.getenv("MEMORY_TOKEN_BUDGET", "3000")))

settings = Settings()
