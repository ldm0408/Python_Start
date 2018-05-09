a= [[1,2],[2,3]]
b = [[3,4],[5,6]]
list1 = []
for x,y in zip(a,b):
    print (x,y)
    for c,d in zip(x,y):
        print(c+d)
        A = [c+d]
        list1 += A

print(list1)

