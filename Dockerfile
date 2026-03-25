FROM python:3.10-slim

# 파이썬 출력을 실시간으로 보기 위한 설정
ENV PYTHONUNBUFFERED=1

# [추가] 시스템 시간대를 한국 표준시(KST)로 기본 설정
ENV TZ=Asia/Seoul

WORKDIR /app

# 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사 (.env 파일 포함됨)
COPY . .

# 데이터 저장 폴더 생성
RUN mkdir -p /app/data

# 디스코드 봇 실행
CMD ["python", "-m", "app.main"]
