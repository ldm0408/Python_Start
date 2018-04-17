list2 = [34, 25, 35, 7, 7, 6]

list2.append(16) # 리스트에 자료 추가 / list2 의 값이 바뀌는것
print(list2)
list3 = list2 + [16] # 이런 방법도 가능 / 새로운 리스트 생성
print(list3)

n = 12
ownership = n in list3 # in 연산자를 이용 리스트 안에 해당 값이 있는지 판별
print(ownership)

n = 34
if n in list2:
    print('{}은 있다'.format(n))

print(list3)
del(list3[-1]) # 리스트 내 특정 순서의 값을 삭제
print(list3)

list2.remove(7) #리스트 내 특정 값을 삭제 / 리스트 내 해당 값이 중복일 경우 맨 앞의 값만 삭제
print(list2)