# 예외를 잡아서 처리하는 법
# 파이썬 예외 이름을 알아두면 좋다
text = '100%'
try:
    number = int(text)
except ValueError:
    print('{}은 숫자가 아니네요'.format(text))

def safe_pop_print(list,index):
        try:
            print(list.pop(index))
        except IndexError:
            print('{} index값을 가져올 수 없어'.format(index))
safe_pop_print([1,2,3],5)
# 경우에 따라 if else 문으로 처리 가능 하다

# 아래의 경우 try except 구문으로만 처리 가능하다
try:
    import my_module1
except ImportError:
    print('모듈 노노')