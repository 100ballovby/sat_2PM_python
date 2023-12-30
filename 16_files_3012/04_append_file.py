with open("test.txt", "a") as f:
    string = input('Введите что-то: ')
    f.write('\n' + string)

with open('test.txt', 'r') as file:
    print(f'В файле теперь написано:\n {file.read()}')


