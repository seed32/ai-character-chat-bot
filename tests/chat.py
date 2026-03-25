import json
import requests

def interactive_chat():
    # Note: This test script is for the legacy FastAPI structure.
    # For the current Discord bot, please run `python -m app.main` directly.
    url = "http://localhost:8080/kakao/callback"
    user_id = "test_user_local"
    
    print("=== AI Character Bot Test Interface ===")
    
    while True:
        utterance = input("\n[User]: ")
        if utterance.lower() in ["exit", "quit", "exit"]:
            break
            
        payload = {
            "userRequest": {
                "utterance": utterance,
                "user": {
                    "id": user_id
                }
            }
        }
        
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                result = response.json()
                answer = result["template"]["outputs"][0]["simpleText"]["text"]
                print(f"[AI]: {answer}")
            else:
                print(f"Error: {response.status_code}")
        except Exception as e:
            print(f"Connection failed: {e}")

if __name__ == "__main__":
    interactive_chat()
