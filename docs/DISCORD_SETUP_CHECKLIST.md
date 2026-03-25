# 🏁 Discord Bot Setup Checklist (디스코드 봇 설정 체크리스트)

Follow these steps to get your bot up and running.
봇을 정상적으로 가동하기 위한 필수 체크리스트입니다.

---

## 🇺🇸 English
1.  **Discord Developer Portal**:
    - [ ] Create a New Application.
    - [ ] Reset/Copy the **Bot Token**.
    - [ ] Enable **Message Content Intent** under the Bot tab.
2.  **Environment (.env)**:
    - [ ] Fill in `DISCORD_TOKEN`.
    - [ ] Fill in at least one `GEMINI_API_KEY`.
    - [ ] Set `ALLOWED_USER_ID` to your Discord ID for security.
3.  **Docker**:
    - [ ] Build the image using `docker build -t ai-character-bot .`.
    - [ ] Export to tar and upload to Synology if deploying remotely.

---

## 🇰🇷 한국어
1.  **디스코드 개발자 포털**:
    - [ ] 새로운 애플리케이션(Application) 생성.
    - [ ] **봇 토큰(Bot Token)** 복사.
    - [ ] Bot 메뉴에서 **Message Content Intent** 스위치 켜기 (필수!).
2.  **환경 변수 (.env)**:
    - [ ] `DISCORD_TOKEN` 입력.
    - [ ] 최소 하나 이상의 `GEMINI_API_KEY` 입력.
    - [ ] 보안을 위해 본인의 디스코드 ID를 `ALLOWED_USER_ID`에 입력.
3.  **도커 (Docker)**:
    - [ ] `docker build -t ai-character-bot .` 명령어로 이미지 빌드.
    - [ ] 시놀로지 배포 시 `.tar` 파일로 추출 후 업로드.
