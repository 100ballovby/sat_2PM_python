import random as r

lst1 = []
for i in range(100):  # повторить 100 раз
    n = r.randint(1, 100)  # сгенерировать случайное целое число
    lst1.append(n)


for i in range(len(lst1) - 1):
    for j in range(len(lst1) - i - 1):
        if lst1[j] > lst1[j + 1]:  # если текущий элемент массива больше следующего
            lst1[j], lst1[j + 1] = lst1[j + 1], lst1[j]


print(lst1)

