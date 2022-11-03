"""
9. Треугольник задан длинами сторон. Найти длины медиан.
"""

from math import *

a, b, c = float(input()), float(input()), float(input())

m_a = sqrt(2*b**2 + 2*c**2 - a**2)/2
m_b = sqrt(2*a**2 + 2*c**2 - b**2)/2
m_c = sqrt(2*a**2 + 2*b**2 - c**2)/2

print('{:.3f} {:.3f} {:.3f}'.format(m_a,m_b,m_c))