n = int(input('Количество ступенек: '))


for line in range(1, n + 1):
    for star in range(1, line + 1):
        print('*', end=' ')
    print()