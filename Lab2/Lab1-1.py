"""
1. Даны числа а1, b1, c1, а2, b2, c2, напечатать точки пересечения прямых, 
заданных уравнениями прямых a1x+b1y+c1=0 и a2x+b2y+c2=0, либо 
сообщить, что эти прямые совпадают, или не пересекаются, или не 
существуют.
"""

a1, b1, c1, a2, b2, c2 = float(input()), float(input()), float(input()), float(input()), float(input()), float(input())

if b1 != 0 and b2 != 0:
    if a1/b1 == a2/b2 and c1/b1 == c2/b2:
        print('прямые совпадают')
    elif a1/b1 == a2/b2 and c1/b1 != c2/b2:
        print('прямые не пересекаются')
    else:
        x = (c1/b1-c2/b2)/(a2/b2-a1/b1)
        y = (-c1/b1-a1*x/b1)
        print(x, y, sep=' ')
else:
    if b1 == 0 and b2 == 0:
        if a1 != 0 and a2 != 0:
            if a2 / a1 == c2/c1:
                print('прямые совпадают')
            else:
                print('прямые не пересекаются')
        else:
            print('хотя бы одна прямая не существует')
    else:
        if b1 == 0 and b2 != 0:
            x = -c1 / a1
            y = -c2 / b2 - a2 * x / b2
            print(x, y, sep=' ')
        elif b1 != 0 and b2 == 0:
            x = -c2 / a2
            y = -c1 / b1 - a1 * x /b1
        