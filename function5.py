def root(a, b, c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2*a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2*a)

    return r1, r2


x = 1
y = 2
z = -8

r1, r2 = root(x,y,z)
print('근은 {},{}'.format(r1, r2))

#return 뒤에 여러 값을 쉼표로 구분해서 값을 보내고, 받을때도 쉼표로 구분하여 받는다.
