"""
Написать программу, которая выводит таблицу значений функции S(x) для х, 
изменяющихся в интервале от x1 до x2 с шагом h.  Переменная N – задает 
количество слагаемых для каждого аргумента х из интервала от х1 до х2 для 
функции S(x). Значение переменной h можно подсчитать по формуле h=(x2 – 
x1)/m, где m – количество точек табуляции переменной  x. 
"""
from math import *

x1, x2, m = int(input()), int(input()), int(input())
print('S(x)   x    N')

i = x1
while i <= x2:
    N = int(input())
    s = 0
    for k in range(N+1):
        s += (-1)**k*i**(2*k+1)/factorial(2*k+1)
    print('{:.3f} {} {}'.format(s, i, N))
    i = i + (x2-x1)/m