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
2.  **Installation**: 
    - Go to **Installation** tab on the left sidebar.
    - Uncheck **"User Install"**.
    - Click **"Install Link"** dropdown -> Select **"None"**.
    - Click **"Save Changes"**.
3.  **Bot Settings**:
    - Go to **Bot** tab on the left sidebar.
    - Click **"Reset Token"** and **Copy** your token (Save it safely!).
    - Scroll down to **"Privileged Gateway Intents"** -> Toggle **"Message Content Intent"** to **ON** (Crucial! ⭐).
    - Toggle **"Public Bot"** to **OFF** (Keep it private).
    - Click **"Save Changes"**.
4.  **OAuth2 (Invite to Server)**:
    - Go to **OAuth2** -> **URL Generator**.
    - **Scopes**: Select **`bot`**.
    - **Bot Permissions**: Select **`Administrator`**.
    - **Copy** the generated URL at the bottom.
    - Paste the URL into your browser and invite the bot to your server.

### 🇰🇷 한국어
1.  **봇 등록**: [디스코드 개발자 포털](https://discord.com/developers/applications)에서 **"New Application"**을 클릭하여 생성합니다.
2.  **설치 설정 (Installation)**:
    - 왼쪽 메뉴에서 **Installation** 탭으로 이동합니다.
    - **"User Install"** 체크를 해제합니다.
    - **"Install Link"** 드롭다운을 클릭하여 **"None" (없음)**으로 변경합니다.
    - 우측 하단 **"Save Changes"**를 눌러 저장합니다.
3.  **봇 설정 (Bot)**:
    - 왼쪽 메뉴에서 **Bot** 탭으로 이동합니다.
    - **"Reset Token"**을 눌러 토큰을 발행하고 **복사**해둡니다. (절대 외부에 노출하지 마세요!)
    - 하단의 **"Privileged Gateway Intents"** 섹션에서 **"Message Content Intent"** 스위치를 **ON**으로 켭니다. (필수! ⭐)
    - **"Public Bot"** 스위치를 **OFF**로 끕니다. (본인만 사용하는 비공개 봇 설정)
    - 우측 하단 **"Save Changes"**를 눌러 저장합니다.
4.  **서버 초대 (OAuth2)**:
    - 왼쪽 메뉴에서 **OAuth2** -> **URL Generator**로 이동합니다.
    - **Scopes**: **`bot`** 항목을 체크합니다.
    - **Bot Permissions**: **`Administrator` (관리자)** 항목을 체크합니다.
    - 맨 아래 생성된 **Generated URL**을 복사합니다.
    - 브라우저 주소창에 붙여넣어 본인의 디스코드 서버로 봇을 초대합니다.

---

## 🆔 3. Getting Your Discord User ID (본인의 디스코드 ID 확인 방법)

To secure your bot, you need your unique Discord User ID for the `ALLOWED_USER_ID` field.
보안을 위해 `ALLOWED_USER_ID`에 입력할 본인의 디스코드 고유 ID가 필요합니다.

### 🇺🇸 English
1. Open Discord **Settings** -> **Advanced**.
2. Enable **"Developer Mode"**.
3. Right-click your profile icon (or name) and click **"Copy User ID"**.
4. Paste this ID into your `.env` file.

### 🇰🇷 한국어
1. 디스코드 **사용자 설정** -> **고급** 메뉴로 이동합니다.
2. **"개발자 모드"**를 활성화합니다.
3. 본인의 프로필 아이콘(또는 이름)에 마우스 오른쪽 버튼을 클릭하고 **"사용자 ID 복사"**를 클릭합니다.
4. 복사된 ID를 `.env` 파일의 `ALLOWED_USER_ID` 항목에 입력합니다.

---

## 🖥️ 4. Launching the Bot (기동 방법)

Choose the method that best fits your environment.
자신의 환경에 맞는 방법을 선택하여 봇을 기동하세요.

### 🍎 Method A: General (Python/Local)
Recommended for development, Windows, or a personal PC.
개발용, 윈도우, 혹은 개인 PC에서 실행할 때 추천합니다.

#### 🇺🇸 English
1.  **Install Python 3.10+**: Make sure Python is in your PATH.
2.  **Clone & Install Dependencies**:
    ```bash
    git clone https://github.com/seed32/chat-bot.git
    cd chat-bot
    pip install -r requirements.txt
    ```
3.  **Prepare .env**: Copy `env.example.kor` (or `.eng`) to `.env` and fill in your keys.
4.  **Run**:
    ```bash
    python -m app.main
    ```

#### 🇰🇷 한국어
1.  **Python 3.10 이상 설치**: 파이썬이 설치되어 있어야 합니다.
2.  **종속성 설치**: 터미널(CMD/PowerShell)에서 아래 명령어를 입력합니다.
    ```bash
    git clone https://github.com/seed32/chat-bot.git
    cd chat-bot
    pip install -r requirements.txt
    ```
3.  **환경 변수 설정**: `env.example.kor` 파일을 복사하여 `.env` 파일을 만들고, 발급받은 키들을 입력합니다.
4.  **실행**:
    ```bash
    python -m app.main
    ```

---

### 🐳 Method B: Docker (Container)
Recommended for 24/7 servers like Synology NAS or a VPS.
시놀로지 NAS, VPS 등 서버에서 24시간 가동할 때 추천합니다.

#### 🇺🇸 English
1.  **Build Image**:
    ```bash
    docker build -t ai-character-bot .
    ```
2.  **Run with Docker Compose (Recommended)**:
    Create a `docker-compose.yml` (template is provided in the root):
    ```bash
    docker-compose up -d
    ```
3.  **Run with Docker Command**:
    ```bash
    docker run -d --name my-ai-bot \
      -v "$(pwd)/.env:/app/.env" \
      -v "$(pwd)/data:/app/data" \
      -e TZ=Asia/Seoul \
      ai-character-bot
    ```

#### 🇰🇷 한국어
1.  **도커 이미지 빌드**:
    ```bash
    docker build -t ai-character-bot .
    ```
2.  **Docker Compose로 실행 (추천)**:
    루트 폴더의 `docker-compose.yml`을 활용하여 백그라운드에서 실행합니다.
    ```bash
    docker-compose up -d
    ```
3.  **Docker 명령어로 직접 실행**:
    ```bash
    docker run -d --name my-ai-bot \
      -v "$(pwd)/.env:/app/.env" \
      -v "$(pwd)/data:/app/data" \
      -e TZ=Asia/Seoul \
      ai-character-bot
    ```

---

## 📊 5. Persistence & Data (데이터 관리)

*   **`data/` folder**: All SQLite databases (`*.db`) are stored here. Do not delete this folder unless you want to wipe all memories.
*   **`.env`**: This file contains your secrets. Never share it publicly.

*   **`data/` 폴더**: 모든 대화 기록(SQLite DB)이 이곳에 저장됩니다. 기억을 초기화하고 싶지 않다면 이 폴더를 삭제하지 마세요.
*   **`.env`**: API 키와 토큰이 들어있으므로 절대 외부에 노출하지 마세요.
