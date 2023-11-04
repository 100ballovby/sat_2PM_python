import random as r
import string

length = int(input('Длина пароля: '))
alphabet = string.ascii_lowercase

print('Выберите, что нужно добавить в пароль:')
print('''
1 - большие буквы
2 - цифры
3 - специальные символы
0 - закончить''')
choice = int(input('Ваш выбор: '))
while choice != 0:
    match choice:
        case 1:
            alphabet += string.ascii_uppercase
        case 2:
            alphabet += string.digits
        case 3:
            alphabet += string.punctuation
    choice = int(input('Добавим что-то еще?'))

passw_num = int(input('Количество паролей: '))
for passw in range(passw_num):
    password = ''
    for i in range(length):
        password += r.choice(alphabet)
    print(password)
