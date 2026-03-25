# ⚙️ Detailed Setup Guide (상세 설정 가이드)

This guide provides step-by-step instructions on obtaining the necessary keys and preparing your backend.
필수 키 발급 및 백엔드 준비를 위한 상세 가이드입니다.

---

## 🔑 1. Getting LLM API Keys (API 키 발급)

### 🇺🇸 English
- **Google Gemini (Highly Recommended)**:
  1. Visit [Google AI Studio](https://aistudio.google.com/).
  2. Log in with your Google account.
  3. Click **"Get API key"** on the left sidebar.
  4. Create a new key and copy it to `GEMINI_API_KEY_1` in your `.env`.
  5. (Optional) Repeat with different Google accounts to bypass rate limits using `GEMINI_API_KEY_2`, etc.

### 🇰🇷 한국어
- **Google Gemini (강력 추천)**:
  1. [Google AI Studio](https://aistudio.google.com/)에 접속합니다.
  2. 구글 계정으로 로그인합니다.
  3. 왼쪽 메뉴에서 **"Get API key"**를 클릭합니다.
  4. 새로운 키를 생성하고 `.env` 파일의 `GEMINI_API_KEY_1` 항목에 복사합니다.
  5. (선택) 사용량 제한을 늘리려면 다른 구글 계정으로 키를 더 발급받아 `GEMINI_API_KEY_2` 등에 넣으세요.

---

## 🖥️ 2. Preparing the Backend (백엔드 준비)

### 🇺🇸 English
This bot needs a continuously running environment to process schedules.
- **Home Server**: Synology NAS (Docker) is the best choice for stability.
- **Cloud**: AWS EC2 (Free Tier), Google Cloud (Compute Engine), or Oracle Cloud (Always Free).
- **Personal PC**: Can be used for testing, but the bot goes offline when the PC is turned off.

### 🇰🇷 한국어
이 봇은 정해진 시간에 메시지를 보내기 위해 24시간 켜져 있는 환경이 필요합니다.
- **가정용 서버**: 시놀로지(Synology) NAS의 도커를 활용하는 것이 가장 안정적이고 저렴합니다.
- **클라우드**: AWS EC2 프리티어, GCP, 오라클 클라우드(무료 티어) 등을 추천합니다.
- **개인 PC**: 테스트용으로는 적합하나, PC를 끄면 봇도 작동을 멈춥니다.

---

## 🤖 3. Discord Bot Registration (디스코드 봇 등록)

### 🇺🇸 English
1. Go to [Discord Developer Portal](https://discord.com/developers/applications).
2. Create **"New Application"**.
3. Go to **"Bot"** tab -> **"Reset Token"** to get your token.
4. **Crucial**: Scroll down to **"Privileged Gateway Intents"** and toggle **"Message Content Intent"** to **ON**.

### 🇰🇷 한국어
1. [디스코드 개발자 포털](https://discord.com/developers/applications)에 접속합니다.
2. **"New Application"**을 눌러 봇을 만듭니다.
3. **"Bot"** 탭으로 가서 **"Reset Token"**을 눌러 토큰을 복사합니다.
4. **필수**: 하단의 **"Privileged Gateway Intents"** 항목에서 **"Message Content Intent"**를 반드시 **ON**으로 켜야 합니다.
