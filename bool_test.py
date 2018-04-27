print(bool(0))
print(bool(1))
print(bool(-1))
print(bool([]))
print(bool([3]))
print(bool(None))
print(bool({}))
print(bool(''))
print(bool('하이'))

value = input("입력해주세요") or '아무것도 못 받았어'
print('입력받은값:',value)
# 앞 부분에 입력 값이 없으면 False 이기 때문에 뒤에로 넘어가는데 뒤는 true이다
# 그래서 뒤의 문자열이 출력 된다
# 하지만 앞 부분에 입력 값을 넣어주면(ex: 하이) 앞 부분이 True가 되어 
# 입력 값인 '하이'가 출력 된다.
