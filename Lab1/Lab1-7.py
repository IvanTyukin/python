"""
7. Найти площадь равнобочной трапеции с основаниями a  и b и углом 
α при большем основании a.
"""

from math import *

a, b, alpha = float(input()), float(input()), float(input())

print('{:.2f}'.format((a+b)*(a-b)*tan(pi*alpha/180)/4))