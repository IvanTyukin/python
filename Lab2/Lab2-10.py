"""
10. Даны координаты точки. А (x, y). Определить,  в какой четверти лежит 
данная точка.
"""

x,y = float(input()), float(input())

if x>0 and y>0:
    print('первая четверть')
elif x>0 and y<0:
    print('четвертая четверть')
elif x<0 and y<0:
    print('третья четверть')
elif x<0 and y>0:
    print('вторая четверть')
else:
    print('центр координат')