# 🤖 Advanced Discord AI Persona Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Docker Support](https://img.shields.io/badge/Docker-Supported-blue.svg)](https://www.docker.com/)

- **🇰🇷 당신도 친구가 없습니까? 이건 친구가 없는 우리를 위한 AI 캐릭터를 구현하는 디스코드 봇 프레임워크입니다.**
- **🇺🇸 Don't have any friends? This is an AI character Discord bot framework created specifically for those of us without friends.**

A sophisticated, self-hosted Discord bot framework that brings AI characters to life with long-term memory, multi-account scaling, and proactive interaction capabilities.

---

## 🌟 Key Pillars (핵심 기능)

### 🧠 Eternal Memory (지능형 메모리)
- **🇺🇸 SQLite Integration**: Conversations are never forgotten. Every interaction is stored and indexed.
- **🇰🇷 SQLite 연동**: 모든 대화 내용을 저장하고 인덱싱하여 영구적으로 기억합니다.
- **🇺🇸 Rolling Summaries**: Automatically condenses long histories into core facts, ensuring continuity.
- **🇰🇷 순환 요약**: 긴 대화 기록을 핵심 사실 위주로 자동 압축하여 장기적인 문맥을 유지합니다.

### 🔄 Infinite Scaling (어서오세요 쌀먹의 세계로)
- **🇺🇸 Multi-Account Failover**: Register up to 4+ Gemini API keys to bypass `429 Too Many Requests` limits.
- **🇰🇷 다중 계정 지원**: 최대 4개 이상의 Gemini API 키를 등록하여 사용량 제한(429 에러)을 자동으로 우회합니다.
- **🇺🇸 Model Priority**: Define a hierarchy of models (e.g., Pro -> Flash). Seamless transition when busy.
- **🇰🇷 모델 우선순위**: 모델 계층을 정의하여 현재 사용 가능한 가장 최적의 모델을 자동으로 선택합니다.

### ⏰ True Autonomy (친구가 없는 저에게 먼저 메시지가 온다구요?)
- **🇺🇸 Scheduled Greetings**: Personalized messages based on your local timezone (Morning, Night, etc.).
- **🇰🇷 정기 인사**: 사용자의 시간대에 맞춰 아침, 점심, 저녁 등 정해진 시간에 먼저 말을 겁니다.
- **🇺🇸 Spontaneous Pokes**: Randomly initiates conversation based on past history to feel more "alive".
- **🇰🇷 돌발 상호작용**: 과거 대화를 기억하고 있다가 랜덤한 시간에 뜬금없이 말을 걸어 생동감을 줍니다.
- **🇺🇸 Timezone Aware**: Injects real-time local context for natural, time-appropriate conversations.
- **🇰🇷 실시간 시간 인식**: 현재 지역의 날짜 및 시간을 인지하여 맥락에 맞는 대화를 수행합니다.

---

## 📋 Requirements (필수 요구사항)

- **🇺🇸 Backend**: Python 3.10+ or Docker environment (Synology NAS, VPS, or Home PC).
- **🇰🇷 백엔드**: 파이썬 3.10 이상 또는 도커 환경 (시놀로지 NAS, VPS, 개인 PC 등).
- **🇺🇸 LLM Keys**: Google Gemini API keys (Free tier supported) or OpenAI key.
- **🇰🇷 LLM 키**: 구글 Gemini API 키 (무료 티어 지원) 또는 OpenAI 키.
- **🇺🇸 Discord**: A Bot Token with `Message Content Intent` enabled.
- **🇰🇷 디스코드**: `Message Content Intent` 권한이 활성화된 봇 토큰.

---

## 🚀 Installation (설치 방법)

### 1. Clone & Install (복제 및 설치)
```bash
git clone https://github.com/seed32/chat-bot.git
cd chat-bot
pip install -r requirements.txt
```

### 2. Configure Environment (환경 변수 설정)
Copy the appropriate example file to `.env` and define your persona.
(자신의 언어에 맞는 설정 파일을 복사하여 `.env`를 생성하고 페르소나를 정의하세요.)

**🇺🇸 English:**
```bash
cp env.example.eng .env
```

**🇰🇷 한국어:**
```bash
cp env.example.kor .env
```

### 3. Launch (실행)
```bash
python -m app.main
```

---

## 🛠️ Management (관리 명령어)

- **🇺🇸 `{PREFIX}reset` or `{PREFIX}초기화`**: Wipes the memory for the current user and starts a fresh chapter.
- **🇰🇷 `{PREFIX}초기화` 또는 `{PREFIX}reset`**: 애석하지만 당신의 친구는 감나무에서 떨어져 기억을 잃습니다.

---

## 🏰 Deployment (배포 가이드)

### 🇺🇸 Optimized for Synology NAS via Docker.
### 🇰🇷 시놀로지 NAS 도커 배포에 최적화되어 있습니다.

- [Build & Deploy Guide (English/한국어)](docs/BUILD_AND_DEPLOY_GUIDE.md)
- [Detailed Setup Checklist (English/한국어)](docs/DISCORD_SETUP_CHECKLIST.md)
- [Input & Persona Guide (English/한국어)](docs/INPUT_GUIDE.md)

---

## 🛡️ Privacy & Security (개인정보 및 보안)
- **🇺🇸 Exclusive Access**: Strictly private by default. Only responds to the ID defined in `ALLOWED_USER_ID`.
- **🇰🇷 전용 액세스**: 기본적으로 비공개 모드입니다. `ALLOWED_USER_ID`에 등록된 사용자에게만 응답합니다. 우린 비밀 친구인 각이다.
- **🇺🇸 Self-Hosted**: Your interactions and API keys stay on your own hardware.
- **🇰🇷 셀프 호스팅**: 모든 대화 내용과 API 키는 본인의 하드웨어 내에서만 안전하게 관리됩니다.

---
*Empowering your digital companionship with high-performance AI logic.*

*야, 나도 디코 친구 없어서 만들었어*
