import math
import random
list = [0,1,2,3,4,5,6,7,8,9]
math.pi
print(math.pi)
a = random.choice(list)

print(a)


def get_web(url):
    """url을 넣으면 페이지 내용을 돌려주는 함수 """
    import urllib.request
    response = urllib.request.urlopen(url)
    data = response.read()
    decode = data.decode('utf-8')
    return decode

url = input('웹 페이지 주소? ')
content = get_web(url)
print(content)
