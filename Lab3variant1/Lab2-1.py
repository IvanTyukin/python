"""
1.   Вводится последовательность из N чисел. Найти и вывести те числа, 
запись которых совпадает с последними цифрами записи их квадратов. 
"""

N = int(input())

for i in range(N):
    a = int(input())
    num = a
    k = 0
    while num != 0:
        num //= 10
        k += 1
    if a ** 2 % 10**k == a:
        print(a)
    #if str(a**2)[len(str(a**2)) - len(str(a)):] == str(a):
        #print(a)
    