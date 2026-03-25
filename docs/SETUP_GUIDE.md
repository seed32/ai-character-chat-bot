# ⚙️ Detailed Setup Guide (상세 설정 가이드)

This guide provides step-by-step instructions on obtaining the necessary keys and preparing your Discord bot.
필수 키 발급 및 디스코드 봇 준비를 위한 상세 가이드입니다.

---

## 🔑 1. Getting LLM API Keys (API 키 발급)

### 🇺🇸 English
- **Google Gemini (Highly Recommended)**:
  1. Visit [Google AI Studio](https://aistudio.google.com/).
  2. Log in with your Google account.
  3. Click **"Get API key"** on the left sidebar.
  4. Create a new key and copy it to `GEMINI_API_KEY` in your `.env`.
  5. (Optional) Repeat with different Google accounts to use `GEMINI_API_KEY_1` ~ `4`.

### 🇰🇷 한국어
- **Google Gemini (강력 추천)**:
  1. [Google AI Studio](https://aistudio.google.com/)에 접속합니다.
  2. 구글 계정으로 로그인합니다.
  3. 왼쪽 메뉴에서 **"Get API key"**를 클릭합니다.
  4. 새로운 키를 생성하고 `.env` 파일의 `GEMINI_API_KEY` 항목에 복사합니다.
  5. (선택) 사용량 제한을 늘리려면 다른 계정으로 키를 더 발급받아 `GEMINI_API_KEY_1` ~ `4`에 넣으세요.

---

## 🤖 2. Discord Bot Creation (디스코드 봇 생성 및 설정)

### 🇺🇸 English
1.  **Registration**: Go to [Discord Developer Portal](https://discord.com/developers/applications) and create a **"New Application"**.
2.  **Installation Settings**: 
    - Go to **Installation** tab.
    - Uncheck **"User Install"**.
    - Click **"Install Link"** dropdown -> Select **"None"**.
    - Click **"Save Changes"**.
3.  **Bot Settings**:
    - Go to **Bot** tab.
    - Click **"Reset Token"** and **Copy** your token (Save it safely!).
    - Scroll down to **"Privileged Gateway Intents"** -> Toggle **"Message Content Intent"** to **ON** (Crucial! ⭐).
    - Toggle **"Public Bot"** to **OFF** (For your private use only).
    - Click **"Save Changes"**.
4.  **Invite to Server**:
    - Go to **OAuth2** -> **URL Generator**.
    - **Scopes**: Select `bot`.
    - **Bot Permissions**: Select `Administrator`.
    - **Copy** the generated URL at the bottom.
    - Paste the URL into your browser and invite the bot to your server.

### 🇰🇷 한국어
1.  **봇 등록**: [디스코드 개발자 포털](https://discord.com/developers/applications)에서 **"New Application"**을 클릭하여 생성합니다.
2.  **설치 설정 (Installation)**:
    - 왼쪽 **Installation** 탭으로 이동합니다.
    - **"User Install"** 체크를 해제합니다.
    - **"Install Link"** 드롭다운을 클릭하여 **"None" (없음)**으로 변경합니다.
    - 우측 하단 **"Save Changes"**를 눌러 저장합니다.
3.  **봇 설정 (Bot)**:
    - 왼쪽 **Bot** 탭으로 이동합니다.
    - **"Reset Token"**을 눌러 토큰을 발행하고 **복사**해둡니다. (절대 외부에 노출하지 마세요!)
    - 하단의 **"Privileged Gateway Intents"** 섹션에서 **"Message Content Intent"** 스위치를 **ON**으로 켭니다. (필수! ⭐)
    - **"Public Bot"** 스위치를 **OFF**로 끕니다. (집사님만 사용할 비공개 봇 설정)
    - 우측 하단 **"Save Changes"**를 눌러 저장합니다.
4.  **서버 초대 (OAuth2)**:
    - 왼쪽 **OAuth2** -> **URL Generator** 메뉴로 이동합니다.
    - **Scopes**: **`bot`** 항목을 체크합니다.
    - **Bot Permissions**: **`Administrator` (관리자)** 항목을 체크합니다.
    - 맨 아래 생성된 **Generated URL**을 복사합니다.
    - 브라우저 주소창에 붙여넣어 본인의 디스코드 서버로 영애님을 초대합니다.

---

## 🖥️ 3. Preparing the Backend (백엔드 준비)

### 🇺🇸 English
- **Home Server**: Synology NAS (Docker) is recommended for 24/7 stability.
- **Environment**: Ensure `TZ=Asia/Seoul` is set for proper scheduling.

### 🇰🇷 한국어
- **가정용 서버**: 24시간 가동을 위해 시놀로지(Synology) NAS의 도커를 활용하는 것을 권장합니다.
- **환경**: 정확한 스케줄 메시지를 위해 `TIMEZONE=Asia/Seoul` 설정을 확인하세요.
