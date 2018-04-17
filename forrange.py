# for range 
# range() 함수 - 필요한 만큼의 숫자를 만들어내는 유용한 기능
for i in range(10):
    print(i)

names = ['철수','동민','유진','누리','경율']
for i in range(len(names)): # len()는 리스트의 길이를 출력
    name = names[i]
    print('{}번:{}'.format(i+1,name))

#enumerate - 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능
for i, name in enumerate(names):
    print('{}번:{}'.format(i+1, name))

# for in list : 순회할 리스트가 정해져 있을 때
# fon in range() : 순회할 횟수가 정해져 있을 떄



