def add_10(value):
    if value < 10:
        return 10
    result = value + 10
    return result # return은 실행시 해당 함수가 종료 된다
                  # 즉 함수 내 최초 return 이후의 코드는 실행되지 않는다.
                  # 하지만 if문등을 사용 할 시에는 아니다

n = add_10(2)
print(n)

n = round(1.5)
print(n)