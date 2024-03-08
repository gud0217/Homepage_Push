import requests
import json

def send_kakao_message(api_key, target_user_id, message):
    # KakaoTalk API URL
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    # 헤더에 Authorization 추가
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # 메시지 데이터 생성
    payload = {
        "template_object": json.dumps({
            "object_type": "text",
            "text": message,
            "link": {
                "web_url": "https://your-website-url.com",  # 선택적인 웹 링크
            }
        })
    }

    # 메시지 전송
    response = requests.post(url, headers=headers, data=payload)

    # 응답 출력
    print(response.json())

# 사용자별로 발급받은 KakaoTalk API 키와 전송할 메시지를 설정
api_key = "d8439877a064484ca2af66ba55f108b4"
target_user_id = "gud5223"  # 수신자 KakaoTalk ID 또는 사용자 고유 식별자
message = "안녕하세요, 카카오톡 메시지 전송 테스트입니다."

# 메시지 전송 함수 호출
send_kakao_message(api_key, target_user_id, message)