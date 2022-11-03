"""
 Даны действительные положительные числа a, b, c. По трем 
сторонам с длинами a, b, c можно построить треугольник. Найти углы 
треугольника.
"""

from math import *

a, b, c = float(input()), float(input()), float(input())

alpha = 180*acos((a**2 + c**2 - b**2)/(2*a*c))/pi
betha = 180*acos((a**2 + b**2 - c**2)/(2*a*b))/pi
gamma = 180*acos((b**2 + c**2 - a**2)/(2*b*c))/pi

print(alpha, betha, gamma, sep=' ');