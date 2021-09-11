print("Nhập số: ")
n = int(input())
x = 1
if (n < 2):
    x = 2
elif (n == 2):
    x = 1
elif (n % 2 == 0):
    x = 2
else:
    for i in range(3, n, 1):
        if (n % i == 0):
            x = 2
if x == 1:
    print(" là số nguyên tố")
else:
    print(" không phải là số nguyên tố")