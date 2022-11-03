"""
11. Треугольник задан длинами сторон. Найти радиусы вписанной и 
описанной окружности.
"""

from math import *

a, b, c = float(input()), float(input()), float(input())

p = (a + b + c) / 2


r = sqrt((p-a)*(p-b)*(p-c)/p)
R = a*b*c/(4*sqrt(p*(p-a)*(p-b)*(p-c)))
print('{:.3f} {:.3f}'.format(r, R))