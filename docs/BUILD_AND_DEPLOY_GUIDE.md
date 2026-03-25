# 🤖 Build & Deploy Guide (빌드 및 배포 가이드)

This guide explains how to build and deploy the AI Character Bot.
이 가이드는 AI 캐릭터 봇의 빌드 및 배포 방법을 설명합니다.

---

## 🇺🇸 English Guide

### 1. Prerequisites
*   **Docker Desktop** installed and running.
*   Terminal open in the project root folder.

### 2. Build Docker Image
```powershell
docker build -t ai-character-bot .
```

### 3. Export Image to Tar
```powershell
docker save -o bot-image.tar ai-character-bot:latest
```

### 4. Synology NAS Deployment
1.  **Upload**: Upload `bot-image.tar` to your NAS.
2.  **Import**: Open **Container Manager** -> **Image** -> **Add from file**.
3.  **Run**: Create a container with these mandatory settings:
    *   **Environment**: `TZ` = `Asia/Seoul`
    *   **Volume**: Map your data folder to `/app/data` and your `.env` file to `/app/.env`.

---

## 🇰🇷 한국어 가이드

### 1. 사전 준비사항
*   **Docker Desktop**이 설치되어 있고 실행 중이어야 합니다.
*   터미널이 프로젝트 루트 폴더에서 열려 있어야 합니다.

### 2. 도커 이미지 빌드
```powershell
docker build -t ai-character-bot .
```

### 3. 이미지를 Tar 파일로 내보내기
```powershell
docker save -o bot-image.tar ai-character-bot:latest
```

### 4. 시놀로지(Synology) NAS 배포
1.  **업로드**: `bot-image.tar` 파일을 NAS에 업로드합니다.
2.  **불러오기**: **Container Manager** -> **이미지** -> **추가(파일에서 추가)**를 통해 파일을 선택합니다.
3.  **실행**: 컨테이너를 생성할 때 다음 설정을 반드시 확인하세요:
    *   **환경 변수**: `TZ` = `Asia/Seoul` (시간대 설정)
    *   **볼륨 매핑**: 데이터 폴더를 `/app/data`에, `.env` 파일을 `/app/.env`에 연결합니다.
    *   **권한**: 매핑된 폴더에 쓰기 권한이 있는지 확인하세요.
