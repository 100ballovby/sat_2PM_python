year = int(input('Введите год: '))
# номер года должен быть кратен 4 или 400, но не кратен 100
if (year % 400 == 0) or (year % 4 == 0) and not (year % 100 == 0):
    print(f'{year} високосный')
else:
    print(f'{year} не високосный')