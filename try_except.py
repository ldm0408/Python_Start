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

try:
    import my_module1
except ImportError:
    print('모듈 노노')