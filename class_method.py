class Human():
    '''인간'''

    def create(name, weight):
        person = Human()
        person.name = name
        person.weight = weight
        return person

    def eat(self):
        self.weight += 0.1
        print("{}가 먹어서 {}kg가 되었습니다".format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg가 되었습니다".format(self.name, self.weight))

    def speak (self,message):
        print(message)

'''
self
메소드의 첫번째 인자
인스턴스의 매개변수를 전달 할 때는 self 매개변수는 생략하고 전달
'''

person = Human.create('영수', 78)

person.walk()  # 인스턴스의 매개변수를 전달 할 때는 self 매개변수는 생략하고 전달
person.eat()
person.walk()
person.speak('안녕하세요')
