from openai import OpenAI, RateLimitError
from app.config import settings

class LLMClient:
    def __init__(self) -> None:
        self.provider = settings.llm_provider.strip().lower()
        self.clients = []
        
        # 사용 가능한 모든 키로부터 클라이언트 생성
        all_keys = [settings.gemini_api_key] + settings.gemini_api_keys
        # 중복 제거 및 빈 값 제거
        unique_keys = list(dict.fromkeys([k for k in all_keys if k]))
        
        if self.provider == "gemini":
            for key in unique_keys:
                self.clients.append(OpenAI(api_key=key, base_url=settings.gemini_base_url))
        else:
            if settings.openai_api_key:
                self.clients.append(OpenAI(api_key=settings.openai_api_key))

        self.enabled = len(self.clients) > 0

    def chat(self, messages: list[dict]) -> str:
        if not self.enabled:
            return "설정된 API 키가 없습니다."

        # 시도할 모델 리스트
        models_to_try = [
            settings.llm_model_priority_1,
            settings.llm_model_priority_2,
            settings.llm_model_priority_3,
            settings.llm_model_chat
        ]

        last_error = None
        
        # 1단계: 모델 순회
        for model_name in models_to_try:
            if not model_name: continue
            
            # 2단계: 해당 모델에 대해 모든 키 순회
            for idx, client in enumerate(self.clients):
                try:
                    print(f"[*] 시도 중... 모델: {model_name} (계정 {idx+1}/{len(self.clients)})")
                    response = client.chat.completions.create(
                        model=model_name,
                        messages=messages,
                        temperature=0.8,
                    )
                    return response.choices[0].message.content or ""
                except RateLimitError:
                    print(f"[!] 사용량 초과 (계정 {idx+1}). 다음 계정으로 시도합니다.")
                    continue # 다음 키로 시도
                except Exception as e:
                    print(f"[!] 기타 에러 발생: {e}")
                    last_error = e
                    # 다른 키로 시도해도 마찬가지일 확률이 높으므로 다음 모델로 패스
                    break 
            
            print(f"[-] 모델 {model_name}의 모든 계정이 사용량 초과입니다. 다음 모델로 넘어갑니다.")

        raise last_error or Exception("모든 모델과 계정 호출에 실패했습니다.")

    def summarize(self, text: str, existing_summary: str) -> str:
        if not self.enabled:
            return (existing_summary + "\n" + text).strip()[-1500:]

        prompt = [
            {"role": "system", "content": "You compress chat memory. Output concise bullet points."},
            {"role": "user", "content": f"Summary:\n{existing_summary}\n\nChunk:\n{text}\n\nReturn <= 12 bullets."}
        ]
        try:
            return self.chat(prompt)
        except:
            return existing_summary
