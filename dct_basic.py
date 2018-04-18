#딕셔너리
# 리스트 처럼 여러 값을 저장해두고 필요한 값을 꺼내쓰는 기능

wintable = {
    '가위' : '보',
    '바위' : '가위',
    '보' : '바위'
}
# 리스트 처럼 인덱스로 호출 되지 않음 - 이름표로 호출 함
print(wintable['가위'])  

def rsp(mine, yours):
    if min == yours:
        return 'draw'
    elif wintable[mine] == yours:
        return 'win'
    else:
        return 'lose'

result = rsp('가위','바위')
print(result)

messages = {
    'win' : '이겼다',
    'draw': '비겼다',
    'lose': '졌다'
}

print(messages[result])   
