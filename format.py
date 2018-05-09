# 인사 로봇
# 문자열.format() 문자열을 만드는데 더 효과적인 방법
#문자열의 대괄호 자리에 format 뒤의 괄호안에 들어있는 값을 하나씩 넣는다
#문자열에 포함된 대괄호 개수 보다 format안에 들어 있는 값의 수가 많으면 정상 동작
number = 10
greeting = '안녕하세요'
place = '문자열 포맷'
welcome = '환영합니다'

print(number,'번 손님', greeting, '.', place, '에 오신 것을', welcome)

base = '{}번 손님, {}. {}에 오신 것을 {} !'
new_way = base.format(number,greeting,place,welcome)

print(base)
print(new_way)
