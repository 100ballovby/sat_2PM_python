with open("test.txt", "w") as f:
    string = input('Введите что-то: ')
    f.write(string)

with open('test.txt', 'r') as file:
    print(file.read())



