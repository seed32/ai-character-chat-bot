import json
import requests

def test_callback():
    url = "http://localhost:8080/kakao/callback"
    payload = {
        "userRequest": {
            "utterance": "안녕! 넌 누구니?",
            "user": {
                "id": "test_user_123"
            }
        }
    }
    
    try:
        response = requests.post(url, json=payload)
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_callback()
