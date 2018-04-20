# 에러의 이름을 모르는 경우 처리 하는 법
# except를 비워 두고 print()로 에러 발생 표시
# 어떤 에러인지 알기 위해 except Exception as ex: 이런식으로 작성
try:
    list = []
    print(list)

    text = 'abc'
    number = int(text)
except Exception as ex:
    print('에러 발생',ex)
