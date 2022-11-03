"""
2.  Найти все трехзначные числа, такие, что сумма цифр равна А, а само 
число делится на В (А и В вводятся с клавиатуры).
"""

A, B = int(input()), int(input())

for i in range(100,1000):
    result = 0
    k = i
    while k // 10 != 0:
        result += k % 10
        k //= 10
    result += k
    if result == A and i % B == 0:
        print(i)