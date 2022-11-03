"""
9. На оси ОХ расположены три точки а, b, с. Определить, какая из точек b 
или с расположена ближе к а.
"""

a,b,c = float(input()), float(input()), float(input())

if abs(b-a)<=abs(c-a):
    print('точка b')
else:
    print('точка c')