with open('pi_million_digits.txt', 'r') as file:
    pi_string = ''
    for line in file.readlines():
        pi_string += line.strip()  # strip() убирает пробелы и другие лишние символы ПО БОКАМ СТРОКИ

print(pi_string)
print(f'Длина: {len(pi_string)}')

date = input('Введите свою дату рождения в формате ДДММГГ:')
if date in pi_string:
    print('Ваша дата рождения найдена в числе π')
else:
    print('Даты рождения нет в числе π')
