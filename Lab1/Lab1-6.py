"""
6. Треугольник задан величинами своих углов и радиусом описанной 
окружности. Найти стороны треугольника.
"""

from math import *

alpha, betha, gamma, R = float(input()), float(input()), float(input()), float(input())

print('{:.2f} {:.2f} {:.2f}'.format(2*R*sin(pi*alpha/180), 2*R*sin(pi*betha/180), 2*R*sin(pi*gamma/180)))