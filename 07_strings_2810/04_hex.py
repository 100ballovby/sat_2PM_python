number = input('Введите число: ')
base = int(input('Введите основание системы (до девятиричной): '))

hexadecimal = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}

power = len(number) - 1
decimal_number = 0

for i in range(len(number)):
    try:
        digit = int(number[i])
    except ValueError:
        digit = int(hexadecimal[number[i].upper()])
    decimal_number += digit * (base ** power)
    power -= 1

print(decimal_number)

