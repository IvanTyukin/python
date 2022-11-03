"""
Вариант 1
В одномерном массиве, состоящем из п вещественных элементов, 
вычислить:
количество и сумму отрицательных элементов массива;
наименьшее положительное нечетное число;
произведение двузначных элементов массива, которые не делятся на 6.
"""

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))
    
count, summ = 0, 0
minpositiv = max(arr)
compositiond = 1
for i in range(n):
    if arr[i] < 0:
        summ += arr[i]
        count += 1
    if 0 < arr[i] < minpositiv and arr[i] % 2 == 1:
        minpositiv = arr[i]
    if 10<=arr[i]<=99 and arr[i] % 6 != 0:
        compositiond *= arr[i]

print(count,summ)
print(minpositiv)
print (compositiond)