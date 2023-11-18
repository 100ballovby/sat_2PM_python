import random as r

matrix = []
for i in range(6):
    line = []
    for j in range(6):
        line.append(r.randint(1, 100))
    matrix.append(line)

print(matrix)

sum_min = 0
sum_max = 0

for i in range(len(matrix)):
    print(matrix[i])
    if i % 2 == 0:
        sum_max += max(matrix[i])
    else:
        sum_min += min(matrix[i])

print(f'Сумма максимальных элементов четных строк: {sum_max}')
print(f'Сумма минимальных элементов нечетных строк: {sum_min}')


