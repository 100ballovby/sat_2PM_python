number = input('Введите число: ')
base = int(input('Введите основание системы (до девятиричной): '))

power = len(number) - 1
decimal_number = 0

for i in range(len(number)):
    decimal_number += int(number[i]) * (base ** power)
    power -= 1

print(decimal_number)

