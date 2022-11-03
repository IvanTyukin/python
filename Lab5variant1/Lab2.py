"""
Вариант 1 
1. Дана матрица размера M × N и целые числа K1 и K2 (1 ≤ K1 
< K2 ≤ M). Поменять местами строки матрицы с номерами K1 и K2. 
2. Дана матрица размера M × N. Удалить строку, содержащую 
минимальный элемент матрицы.
3. Дана матрица размера M × N. Вставить в нее столбец из 
некоторого числа K  перед столбцом, содержащим наибольшее 
количество нулевых элементов.
"""


# 1. 
m, n = int(input()), int(input())

k1,k2 = int(input()), int(input())

matrix = [0] * m
for i in range(m):
    matrix[i] = [0] * n
    
for i in range(m):
    for j in range(n):
        matrix[i][j] = int(input())
    
for j in range(n):
    matrix[k1 - 1][j], matrix[k2 - 1][j] = matrix[k2 - 1][j], matrix[k1 - 1][j]
    
for i in range(m):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()

# 2.Дана матрица размера M × N. Удалить строку, содержащую минимальный элемент матрицы.
minimum = matrix[0][0]
imax, jmax = 0, 0
for i in range(m):
    for j in range(n):
        if matrix[i][j] < minimum:
            minimum = matrix[i][j]
            imin = i
            jmin = j
del matrix[imin]

print('Матрица, где удалена строка с минимальным элементом: ')
for i in range(m - 1):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()

# 3.

print('Введите k')
k = int(input())
matrix1 = [0] * m
for i in range(m):
    matrix1[i] = [0] * n
    
print('Введите элементы матрицы')
for i in range(m):
    for j in range(n):
        matrix1[i][j] = int(input())
        
maxzero = 0
jmaxzero = 0
for i in range(n):
    count = 0
    for j in range(m):
        if matrix1[j][i] == 0: 
            count += 1
    if count > maxzero:
        maxzero = count
        jmaxzero = i
        
for i in range(m):
    matrix1[i].insert(jmaxzero, k)
    
print('Ответ на третью задачу: ')
for i in range(m):
    for j in range(n+1):
        print(matrix1[i][j], end=' ')
    print()