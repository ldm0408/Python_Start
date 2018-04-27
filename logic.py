def return_false():
    print("함수 리턴 false")
    return False

def return_true():
    print("함수 리턴true")
    return True

print("테스트1")

a = return_false
b = return_true

if a and b:
    print(True)
else:
    print(False)

print("테스트 2")

if return_false() and return_false():
    print("true")
else:
    print(False)
# 단락 평가 
# 논리연산에서 코드의 앞만 보고 값을 정할 수 있는 경우 뒤는 보지 않고 값을 결정

dic = {"key2": "vlaue1"}

if "key1" in dic and dic["key1"] == "value1":
    print("key1 있고, 값은 value1 이다")
else: 
    print("아니네")

# 복잡한 코드를 단순하게 해준다.
