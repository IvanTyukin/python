"""
10. Треугольник задан длинами сторон. Найти длины биссектрис. 
"""

from math import *

a, b, c = float(input()), float(input()), float(input())

l_a = sqrt(a*b*(a+b+c)*(a+b-c))/(b+c)
l_b = sqrt(a*b*(a+b+c)*(a+b-c))/(a+c)
l_c = sqrt(a*b*(a+b+c)*(a+b-c))/(a+b)

print('{:.3f} {:.3f} {:.3f}'.format(l_a, l_b, l_c))