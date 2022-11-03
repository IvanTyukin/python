"""
Даны 8 различных чисел. Определить максимальное из них, используя
функцию определения максимального из двух чисел.
"""

def maximum(a, b):
    if a>b:
        return a
    else:
        return b

maxnum = int(input())
i = 1
while i < 8:
    a2 = int(input())
    i += 1
    maxnum = maximum(maxnum, a2)
    
print("Максимальное число среди введенных", maxnum)