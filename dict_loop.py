# 딕셔너리 이용한 반복문

ages = {
    'tod' : 35,
    'paul' : 62,
    'jane' : 24
}

for key in ages:
    print('{}의 나이는{}'.format(key,ages[key]))

for key,value in ages.items():
    print('{}의 나이는{}'.format(key, value))

# 딕셔너리의 반복문은 순서가 매번 일정 하지 않는다(값의 순서를 지키지 않는다)
# 일정한 순서를 지킨 반복문을 사용하려면 리스트가 더 낫다