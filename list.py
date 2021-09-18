list = [2, 6, 3, 8, 1, 4, 7]
for i in range(0, 6):
    for j in range(i + 1, 7):
        if (list[i] > list[j]):
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
print(list)