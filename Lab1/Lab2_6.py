"""
6) среди чисел a, b, c, d есть взаимно противоположные;
"""

a, b, c, d = float(input()), float(input()), float(input()), float(input())

print(abs(a) == abs(b) or abs(a) == abs(c) or abs(a) == abs(d) or abs(b) == abs(c) or abs(b) == abs(d) or abs(c) == abs(d))