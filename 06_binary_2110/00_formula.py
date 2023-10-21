n = input('Введи бинарное число: ')

b = 8
r = int(n[0])  # первую цифру двоичного числа перевожу в число

for i in range(1, len(n)):
    r = r * b + int(n[i])
print(r)





