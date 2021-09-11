a = float(input('Nhap a: '))
while a == 0:
    if a == 0:
        print('Nhap a!')
        a = float(input('Nhap a: '))
b = float(input('Nhap b: '))
while b == 0:
    if b == 0:
        print('Nhap b!')
        b = float(input('Nhap b: '))
c = float(input('Nhap c: '))

delta = b * b - 4 * a * c
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print('Phuong trinh co 2 la:')
    print('x1 = ', x1)
    print('x2 = ', x2)
elif delta == 0:
    x = -b / (2 * a)
    print('Phuong trinh co nghiem kep la: x1 = x2 = ', x)
else:
    print('Phuong trinh vo nghiem')