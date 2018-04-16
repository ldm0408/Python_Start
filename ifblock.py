# 블록은 콜론 문자( : )뒤에서 반드시 들여쓰기 (4칸 권장)
if True:
    print('블럭에 속한 코드')
    if False:
        print('한 줄 더') #블록 내 블록 생성 가능
    if True:
        print('마 지 막')
    print('블럭의 끝 코드')
    # 들여쓰기 어긋날 경우 문법 오류 !!!

#다음 블록 작성시 다시 처음으로 내어쓰기 해야 함
print ('새로운 블럭')
    
if False: #블록의 시작의 조건이 안맞으면 블록 안 코드는 실행 하지 않는다
    print('조건이 안 맞는 코드')

    if True:
        print('조건이 맞는 코드')
    
    print('어쨋든 실행 되지 않는 코드')

print('바깥에 있는 코드')


# 블럭
# 함께 실행 되는 하나의 코드 덩어리
# 들여쓰기로 블럭을 구분한다.
# 들여쓰기가 어긋나면 오류가 발생한다.
# 블럭 안에 다른 블럭이 들어갈 수 있다.
# 내부의 블럭은 외부의 블럭에 종속적
# 파이썬 코드 전체를 하나의 블럭으로 볼 수 있다.
