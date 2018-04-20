list = [1,2,3,5,7,2,5,237,55]
for val in list:
    if val % 3 == 0:
        print(val)
        break # 상위 불록 중 첫 번째 반복문을 찾아서 반복문을 종료

# for i in range(10):
#     if i % 2 != 0:
#         print(i)
#         print(i)
#         print(i)
#         print(i)

for i in range(10):
    if i % 2 == 0:
        continue #제외 하는 경우를 첫번쨰로 처리, 핵심 블록이 깊이 들어감을 방지
    print(i)
    print(i)
    print(i)
    print(i)

# for와 while문 둘 다 사용 가능하다