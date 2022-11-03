"""
Написать программу не используя условный оператор. На экран 
вывести TRUE или FALSE
1) x лежит вне отрезков [a, b] и [c, d];
"""

a, b, c, d, x = float(input()), float(input()), float(input()), float(input()), float(input())

print(x>a and x<b or x<d and x>c)