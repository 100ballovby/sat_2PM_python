import random as r

lst1 = []
for i in range(50):  # повторить 100 раз
    n = r.randint(1, 100)  # сгенерировать случайное целое число
    lst1.append(n)

print(lst1)
search = int(input('Введите искомое значение: '))
f_index = 0
found = False  # индикатор нахождения элемента в массиве
"""Линейный поиск - последовательное сравнение искомого значения с каждым элементом
массива/списка. Поиск прекращается при нахождении первого совпадения."""
for i in range(len(lst1)):
    if search == lst1[i]:  # если мы нашли элемент, который по значению совпадает с искомым
        f_index = i  # сохраняем индекс элемента
        found = True  # переключаем индикатор
        break  # принудительный выход из цикла

if found:
    print('Элемент найден, индекс', f_index)
else:
    print('Такого элемента нет')