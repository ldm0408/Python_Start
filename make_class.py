class Human():
    '''사람'''

person1 = Human()
person2 = Human()

person1.language = '한국어'
person2.language = '영어'

person1.name = '서울시민'
person2.name = '인도인'

def speak(person):
    print('{}이 {}로 말을 합니다'.format(person.name, person.language))

Human.speak = speak
person1.speak()  # 서울시민이 한국어로 말을 합니다
person2.speak()  # 인도인이 영어로 말을 합니다

