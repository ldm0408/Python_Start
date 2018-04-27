'''
오버라이드(Override)
같은 이름을 가진 메소드를 덮어 쓴다는 의미
'''
class Animal():
    def walk(self):
        print('걷는다')

    def eat(self):
        print('먹는다')
    
    def greet(self):
        print("인사한다")


class Human(Animal):
    def wave(self):
        print('손을 흔든다')
    
    def greet(self):
        self.wave()


class Dog(Animal):
    def wag(self):
        print('꼬리를 흔든다')
    
    def greet(self):
        self.wag()

class Cow(Animal):
    '''소'''


person = Human()
person.greet() # 손을 흔든다 / 메소드 오버라이드 함

dog = Dog()
dog.greet() # 꼬리를 흔든다 / 메소드 오버라이드 함

cow = Cow()
cow.greet() # 인사한다 / 부모 메소드를 그대로 사용
