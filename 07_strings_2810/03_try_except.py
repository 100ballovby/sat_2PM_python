n = input('Введите число: ')

try:  # программа пытается выполнить то, что написано в try
    n = int(n)
    print(n ** 2)
except ValueError:  # в случае возникновения ошибки
    print('Ты ввел не число')

print('Hello')

