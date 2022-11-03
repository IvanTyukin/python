"""
7) среди целых чисел a, b, c есть хотя бы два четных;
"""

a, b, c = int(input()), int(input()), int(input())

print(a%2 + b%2 +c%2 < 2)

"""
8) из отрезков с длинами a, b, c можно построить треугольник;
"""

print(a+b>c and b+c>a and a+c>b)