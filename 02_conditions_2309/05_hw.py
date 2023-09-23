x = int(input('Введите двузначное число: '))
units = x % 10
tens = x // 10
print(f'{tens} + {units} = {tens + units}')

# трехназначные числа
x1 = int(input('Введите трехзначное число: '))
units = x1 % 10
tens = x1 % 100 // 10
hundreds = x1 // 100
print(f'{hundreds} + {tens} + {units} = {hundreds + tens + units}')


