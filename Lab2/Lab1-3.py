"""
3. Даны три числа, не используя функции min и max, упорядочить их по 
убыванию.
"""

a, b, c = float(input()), float(input()), float(input())

if a<=b<=c:
    print(c, b, a, sep=' ')
elif a<=c<=b:
    print(b, c, a, sep=' ')
elif b<=c<=a:
    print(a, c, b, sep=' ')
elif b<=a<=c:
    print(c, a, b, sep=' ')
elif c<=a<=b:
    print(b, a, c, sep=' ')
else:
    print(a, b, c, sep=' ')