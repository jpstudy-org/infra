import base64
import sys

def encode_to_base64():
    """
    사용자로부터 텍스트를 입력받아 Base64로 인코딩하는 무한 루프를 실행합니다.
    """
    print("--- Base64 인코더 ---")
    print("변환할 텍스트를 입력하고 Enter를 누르세요.")
    print("(종료하려면 'exit' 또는 'quit'을 입력하거나, 그냥 Enter를 누르세요)")
    print("-" * 20)

    while True:
        try:
            # 사용자로부터 평문(plain text) 입력받기
            plain_text = input("평문 입력 > ")

            # 종료 조건 확인
            if not plain_text or plain_text.lower() in ['exit', 'quit']:
                print("프로그램을 종료합니다.")
                break

            # 1. 입력된 문자열을 바이트(bytes)로 변환 (UTF-8 형식)
            plain_bytes = plain_text.encode('utf-8')

            # 2. 바이트를 Base64로 인코딩
            base64_bytes = base64.b64encode(plain_bytes)

            # 3. 화면에 출력하기 위해 다시 문자열로 변환
            base64_string = base64_bytes.decode('utf-8')

            print(f"Base64 결과: {base64_string}\n")

        except KeyboardInterrupt:
            # Ctrl+C로 종료 시
            print("\n프로그램을 강제 종료합니다.")
            break
        except Exception as e:
            print(f"오류가 발생했습니다: {e}\n")

if __name__ == "__main__":
    encode_to_base64()