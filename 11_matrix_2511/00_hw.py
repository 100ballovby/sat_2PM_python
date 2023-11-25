import random as r

m1, n1 = r.randint(2, 10), r.randint(2, 10)
matrix1 = []
for i in range(m1):
    line = []
    for j in range(n1):
        line.append(r.randint(1, 100))
    matrix1.append(line)

m2, n2 = r.randint(2, 10), r.randint(2, 10)
matrix2 = []
for i in range(m2):
    line = []
    for j in range(n2):
        line.append(r.randint(1, 100))
    matrix2.append(line)

print(matrix1)
print(matrix2)

if m1 == m2 and n1 == n2:
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    print(result)
else:
    print('Сложение матриц невозможно')

