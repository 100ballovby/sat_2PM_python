x = int(input('Введите число: '))
y = int(input('Введите число: '))

if x > y:  # мы проверяем высказывание о том, что значение х больше значения у
    print(f'{x} наибольшее')  # если это так, то вывести в консоль текст
elif y > x:  # мы проверяем высказывание о том, что значение y больше значения x
    print(f'{y} наибольшее')  # вывести текст в консоль
else:
    print('Числа равны!')

