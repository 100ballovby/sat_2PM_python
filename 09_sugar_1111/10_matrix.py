matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
search = int(input("Enter number: "))
for i in range(len(matrix)):  # перебор строк матрицы
    for j in range(len(matrix[i])):  # перебор столбцов матрицы
        if matrix[i][j] == search:
            print(f'Found in line {i}, index: {j}')
            break
    print()

matrix[1][1] = 89  # замена ТОЛЬКО по двум индексам
print(matrix)
print(matrix[1][1] * matrix[0][2])