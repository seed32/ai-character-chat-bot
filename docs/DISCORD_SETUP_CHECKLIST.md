# 🏁 Discord Bot Setup Checklist (디스코드 봇 설정 체크리스트)

Follow these steps to get your bot up and running.
봇을 정상적으로 가동하기 위한 필수 체크리스트입니다.

---

## 🇺🇸 English
1.  **Discord Developer Portal**:
    - [ ] **Registration**: Create a New Application.
    - [ ] **Installation**:
        - [ ] Uncheck **"User Install"**.
        - [ ] Set **"Installation Link"** to **"None"**.
        - [ ] Click **"Save Changes"**.
    - [ ] **Bot**:
        - [ ] **Reset Token** and copy it.
        - [ ] Enable **"Message Content Intent"** (Mandatory! ⭐).
        - [ ] Disable **"Public Bot"**.
        - [ ] Click **"Save Changes"**.
    - [ ] **OAuth2 (Invite)**:
        - [ ] Go to **URL Generator**.
        - [ ] Select **`bot`** scope.
        - [ ] Select **`Administrator`** permission.
        - [ ] Copy the generated URL and invite the bot to your server.
2.  **Environment (.env)**:
    - [ ] Fill in `DISCORD_TOKEN` with your bot token.
    - [ ] Fill in at least one `GEMINI_API_KEY`.
    - [ ] Set `ALLOWED_USER_ID` to your Discord ID for security.
3.  **Docker**:
    - [ ] Build the image using `docker build -t ai-character-bot .`.
    - [ ] Export to tar and upload to Synology if deploying remotely.

---

## 🇰🇷 한국어
1.  **디스코드 개발자 포털**:
    - [ ] **봇 등록**: 새로운 애플리케이션(Application) 생성.
    - [ ] **설치 설정 (Installation)**:
        - [ ] **"User Install"** 체크 해제.
        - [ ] **"Installation Link"** 드롭다운 -> **"None" (없음)** 선택.
        - [ ] **"Save Changes"** 클릭하여 저장.
    - [ ] **봇 설정 (Bot)**:
        - [ ] **토큰 초기화(Reset Token)** 후 복사해두기.
        - [ ] **"Message Content Intent"** 스위치 켜기 (필수! ⭐).
        - [ ] **"Public Bot"** 스위치 끄기 (OFF).
        - [ ] **"Save Changes"** 클릭하여 저장.
    - [ ] **OAuth2 (서버 초대)**:
        - [ ] **OAuth2 URL Generator** 메뉴 이동.
        - [ ] 스코프(Scopes)에서 **`bot`** 체크.
        - [ ] 봇 권한(Bot Permissions)에서 **`Administrator` (관리자)** 체크.
        - [ ] 생성된 URL을 복사하여 자신의 서버에 초대.
2.  **환경 변수 (.env)**:
    - [ ] `DISCORD_TOKEN`에 복사한 토큰 입력.
    - [ ] 최소 하나 이상의 `GEMINI_API_KEY` 입력.
    - [ ] 보안을 위해 본인의 디스코드 ID를 `ALLOWED_USER_ID`에 입력.
3.  **도커 (Docker)**:
    - [ ] `docker build -t ai-character-bot .` 명령어로 이미지 빌드.
    - [ ] 시놀로지 배포 시 `.tar` 파일로 추출 후 업로드.
