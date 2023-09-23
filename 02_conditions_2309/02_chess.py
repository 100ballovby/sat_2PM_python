"""
Заданы две клетки шахматной доски. Если они покрашены в один
цвет, то выведите слово YES, а если в разные цвета — то
NO. Программа получает на вход четыре числа от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для первой
клетки, потом для второй клетки.
"""
x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))

if (x1 + y1 + x2 + y2) % 2 == 0 and (1 <= x1 <= 8) and (1 <= y1 <= 8) and (1 <= x2 <= 8) and (1 <= y2 <= 8):
    print('YES')
elif not (x1 + y1 + x2 + y2) % 2 == 0 and (1 <= x1 <= 8) and (1 <= y1 <= 8) and (1 <= x2 <= 8) and (1 <= y2 <= 8):  # (x1 + y1 + x2 + y2) % 2 != 0
    print('NO')
else:
    print('ERROR')