# ✍️ Input & Persona Guide (인풋 및 페르소나 가이드)

This guide explains all environment variables available in your `.env` file to customize your AI character.
`.env` 파일에서 AI 캐릭터를 커스터마이징하기 위한 모든 환경 변수를 설명합니다.

---

## 🛠️ 1. LLM & API Settings

### 🇺🇸 English
- **`LLM_PROVIDER`**: Choose `gemini` (recommended) or `openai`.
- **`GEMINI_API_KEY`**: Your primary Google AI Studio key.
- **`GEMINI_API_KEY_1~4`**: (Optional) Additional keys to bypass rate limits.
- **`LLM_MODEL_PRIORITY_1~3`**: Hierarchy of models to try if the primary is busy.
- **`LLM_MODEL_CHAT`**: Default model for conversation.
- **`LLM_MODEL_SUMMARY`**: Default model for memory summarization.

### 🇰🇷 한국어
- **`LLM_PROVIDER`**: `gemini` (추천) 또는 `openai` 중 선택합니다.
- **`GEMINI_API_KEY`**: 구글 AI 스튜디오에서 발급받은 기본 키입니다.
- **`GEMINI_API_KEY_1~4`**: (선택) 할당량 제한을 피하기 위한 추가 키들입니다.
- **`LLM_MODEL_PRIORITY_1~3`**: 1순위 모델이 바쁠 때 순차적으로 시도할 모델 목록입니다.
- **`LLM_MODEL_CHAT`**: 대화에 기본으로 사용할 모델입니다.
- **`LLM_MODEL_SUMMARY`**: 메모리 요약에 기본으로 사용할 모델입니다.

---

## 🤖 2. Discord Settings

### 🇺🇸 English
- **`DISCORD_TOKEN`**: Your bot token from Developer Portal.
- **`DISCORD_CHANNEL_ID`**: Channel ID for proactive messages (0 for DM only).
- **`ALLOWED_USER_ID`**: Your numeric Discord ID (Required for security).
- **`BOT_PREFIX`**: Prefix for commands (e.g., `!`).

### 🇰🇷 한국어
- **`DISCORD_TOKEN`**: 디스코드 개발자 포털에서 발급받은 봇 토큰입니다.
- **`DISCORD_CHANNEL_ID`**: 봇이 먼저 말을 걸 채널 ID입니다 (0이면 개인 DM으로 발송).
- **`ALLOWED_USER_ID`**: 본인의 디스코드 숫자 ID입니다 (보안을 위해 필수 ⭐).
- **`BOT_PREFIX`**: 명령어 접두사입니다 (예: `!`).

---

## 🎭 3. Persona (Character) Settings

### 🇺🇸 English
- **`PERSONA_NAME`**: The name of your character.
- **`PERSONA_PROFILE`**: Detailed background, hobbies, and personality.
- **`RESPONSE_STYLE`**: Specific instructions on tone and catchphrases.
- **`EMOJI_POLICY`**: Rules for emoji usage.
- **`PERSONA_GUARDRAILS`**: Hard rules the AI must follow (e.g., "Never say you are AI").
- **`BLOCK_TOPICS`**: Forbidden topics.
- **`SENSITIVE_TOPICS_RULE`**: How to refuse forbidden topics in character.

### 🇰🇷 한국어
- **`PERSONA_NAME`**: 캐릭터의 이름입니다.
- **`PERSONA_PROFILE`**: 캐릭터의 배경 스토리, 취미, 성격 등을 상세히 적습니다.
- **`RESPONSE_STYLE`**: 대화 말투, 입버릇 등 구체적인 지침입니다.
- **`EMOJI_POLICY`**: 이모지 사용 빈도와 규칙을 정합니다.
- **`PERSONA_GUARDRAILS`**: AI가 반드시 지켜야 할 규칙입니다 (예: "절대 AI라고 밝히지 말 것").
- **`BLOCK_TOPICS`**: 봇이 대답하지 말아야 할 금지 주제들입니다.
- **`SENSITIVE_TOPICS_RULE`**: 금지 주제에 대해 캐릭터 성격을 유지하며 거절하는 방법입니다.

---

## ⏰ 4. Scheduling & Spontaneity

### 🇺🇸 English
- **`TIMEZONE`**: Your local timezone (e.g., `Asia/Seoul`).
- **`SCHEDULE_TIMES`**: List of times for greetings (e.g., `09:00,12:00`).
- **`SCHEDULE_LABELS`**: Topics for those times (e.g., `Morning,Lunch`).
- **`SPONTANEOUS_CHANCE`**: Probability (0 to 1) of a random poke every hour.
- **`SPONTANEOUS_START/END_HOUR`**: Time range for random pokes.

### 🇰🇷 한국어
- **`TIMEZONE`**: 거주 지역 시간대입니다 (예: `Asia/Seoul`).
- **`SCHEDULE_TIMES`**: 정기 인사를 보낼 시간 목록입니다 (예: `09:00,12:00`).
- **`SCHEDULE_LABELS`**: 각 시간별 대화 주제입니다 (예: `아침,점심`).
- **`SPONTANEOUS_CHANCE`**: 매 시간마다 봇이 먼저 말을 걸 확률 (0~1 사이).
- **`SPONTANEOUS_START/END_HOUR`**: 돌발 메시지를 보낼 시간 범위입니다.

---

## 🧠 5. Memory & System Messages

### 🇺🇸 English
- **`MEMORY_KEEP_RECENT_MESSAGES`**: Number of recent messages to keep in raw format.
- **`MEMORY_TOKEN_BUDGET`**: Token threshold to trigger summarization.
- **`MSG_RESET_CONFIRM`**: Message shown when memory is wiped.
- **`MSG_LLM_ERROR`**: Message shown when the AI service is unavailable.

### 🇰🇷 한국어
- **`MEMORY_KEEP_RECENT_MESSAGES`**: 요약 시 남겨둘 최신 메시지 개수입니다.
- **`MEMORY_TOKEN_BUDGET`**: 요약을 트리거할 토큰 임계치입니다.
- **`MSG_RESET_CONFIRM`**: 기억 초기화(!reset) 시 출력할 대사입니다.
- **`MSG_LLM_ERROR`**: AI 서비스 에러 발생 시 출력할 대사입니다.
