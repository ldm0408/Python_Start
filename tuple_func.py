list = [1,2,3,4,5]
for i,v in enumerate(list):
    print('{}쨰 값: {}'.format(i,v))

for a in enumerate(list):
    print('{}쨰 값: {}'.format(a[0],a[1]))
# enumerate로 튜플이 생성 되고, 이 튜플을 이용해서 format으로 값을 대입
for a in enumerate(list):
    print('{}쨰 값: {}'.format(*a))

ages = {'tod': 35, 'jane': 23, 'paul': 55}
for a in ages.items():
    print(*a)
    print('{}의 나이{}'.format(*a))
# .items()로 튜플을 생성하고, 이 튜플을 이용해서 format으로 값을 대입

