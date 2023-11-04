phrase = input('Введите строку: ')

words = 0
for i in range(len(phrase)):
    if phrase[i] == ' ':
        words += 1
        
print(f'Количество слов: {words + 1}')


