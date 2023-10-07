n = int(input('Введите число: '))

if n >= 0:
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i

    print(f'{n}! = {factorial}')
else:
    print(f'{n} is prohibited')


