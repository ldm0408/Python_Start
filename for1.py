# for in 반복문
# 코드를 필요한만큼 반복해서 실행

patterns = ['가위', '보', '보', '가위', '가위', '보', '가위','바위','보']
for pattern in patterns:  # in 뒤의 모든 값을 in 앞의 변수에 한번씩 넣어가면 블록을 실행
    if pattern == '가위':
        print('비겼다')
    else:
        print(pattern)

