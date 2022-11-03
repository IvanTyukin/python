"""
9) треугольники со сторонами a1, b1, c1 и a2, b2, c2 подобны;
"""

a1, b1, c1, a2, b2, c2 = float(input()), float(input()), float(input()), float(input()), float(input()), float(input())

print(a1/a2==b1/b2 and b1/b2 == c1/c2)