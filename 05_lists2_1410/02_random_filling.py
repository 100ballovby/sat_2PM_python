import random as r

lst1 = []
for i in range(50):  # повторить 100 раз
    n = r.randint(1, 100)  # сгенерировать случайное целое число
    lst1.append(n)

print(lst1)
