# selected = None
# # 해당 조건이 충족 되는 한 계속 블록 구문을 실행 시킨다
# while selected not in ['가위','바위','보']:
#     selected = input('가위,바위,보 중에 선택하세요>')
# print('선택된 값은:',selected)

# # 조건이 맞으면 실행은 되지만 1번밖에 실행 되지 않는다.
# if selected not in ['가위','바위','보']:
#     selected = input('가위,바위,보 중에 선택하세요>')
# print('선택된 값은:',selected)

patterns = ['가위','보','보']
length = len(patterns)
i = 0
while i < length:
    print(patterns[i])
    i = i +1

for i in range(len(patterns)):
    print(patterns[i])
# for문 코드는 while문으로 작성 할 수 있다. 그 때 상황에 맞는 반복문을 사용하자