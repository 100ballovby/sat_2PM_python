cows = int(input('Введите число: '))
word = 'коров'

if cows % 10 == 1:
    word += 'а'
elif cows % 10 in [2, 3, 4] and (cows % 100 < 10 or cows % 100 >= 20):
    word += 'ы'
else:
    word += ''

print(f'{cows} {word}')
