"""
8. Треугольник задан длинами сторон. Найти длины высот.
"""

from math import *

a, b, c = float(input()), float(input()), float(input())

p = (a + b + c) / 2
h1 = 2*sqrt(p*(p-a)*(p-b)*(p-c))/a
h2 = 2*sqrt(p*(p-a)*(p-b)*(p-c))/b
h3 = 2*sqrt(p*(p-a)*(p-b)*(p-c))/c

print('{:.3f} {:.3f} {:.3f}'.format(h1,h2,h3))