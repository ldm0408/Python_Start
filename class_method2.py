class Human():
    '''인간'''

    def __init__(self,name,weight):
        '''초기화 함수'''
        self.name = name
        self.weight = weight

    def __str__(self):
        '''문자열화 함수'''
        return "{} (몸무게 {}kg)".format(self.name, self.weight)

    def eat(self):
        self.weight += 0.1
        print("{}가 먹어서 {}kg가 되었습니다".format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg가 되었습니다".format(self.name, self.weight))

    def speak(self, message):
        print(message)

'''
* __init__(self) 함수
  인스턴스를 만드는 순간에 자동으로 실행되는 함수
  앞서 만들었던 create 메소드 대신 __init__ 함수에 그 내용을 넣어 주면 간결해진다
'''
'''
* __str__(self)함수
  인스턴스 자체를 출력 할 때의 문자열 형식을 지정해주는 함수
'''
person = Human('사람',78)
print(person.name)
print(person.weight)

print(person2)