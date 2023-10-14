import random as r

lst1 = []
for i in range(100):  # повторить 100 раз
    n = r.randint(-1000, 1000)  # сгенерировать случайное целое число
    lst1.append(n)
lst1.sort()  # сортируем массив от меньшего к большему
print(lst1)
search = int(input('Введите искомое значение: '))
low = 0  # первый элемент - самый маленький индекс
high = len(lst1) - 1   # последний элемент - самый большой индекс массива
mid = (high + low) // 2
f_index = 0


while search != lst1[mid] and low < high:  # пока не нашли значение И пока границы массива не схлопнулись
    if search > lst1[mid]:
        low = mid + 1
    elif search < lst1[mid]:
        high = mid - 1
    mid = (high + low) // 2


if search == lst1[mid]:
    f_index = mid
    print('Элемент найден, индекс', f_index)
else:
    print('Такого элемента нет')
print(end - start)
