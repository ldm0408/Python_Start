#List Comprehension
# 한변의 길이가 1 부터 10 까지의 정사각형 각각의 넓이 구할 때

areas = []
for i in range(1,11):
    areas = areas + [i *i]
print(areas)

areas2 = [i*i for i in range(1,11)]
print(areas2)

# 한 변의 길이가 짝수 일 경우만
areas3 = []
for i in range(1, 11):
    if i % 2 == 0:
        areas3 = areas3 + [i * i]
print(areas3)

areas4 = [i*i for i in range(1, 11) if i % 2 == 0] # for 문 뒤에 if 조건을 적어 준다
print(areas4)

# 튜플을 이용하여 15 * 15 바둑판의 좌표 생성하기
list1 = [(x,y) for x in range(15) for y in range(15)]
print(list1)