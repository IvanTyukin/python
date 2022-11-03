from math import *

# 1)

x, y = float(input()), float(input())

print(x**2 + y**2 == 4 or x == 2 or y == x)
# 2)

print(y < sin(x) and 0 <= y <= 0.5)

# 3)

print(x**2+y**2<=1 and(y>=x or y<=x and x<=0))

# 4)

print(y<=x**2 and y>=0 and (x<0 and y>=2-x or x>=0 and y<=2-x))

# 5)

print(x>=0 and y<=1 and y>=x-1 or (x**2+y**2<=1 and y<x-1))

# 6) недостаточно данных
