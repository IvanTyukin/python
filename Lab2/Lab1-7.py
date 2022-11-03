"""
7. Даны вещественные положительные числа a, b, c, x, y.  Выяснить,  
пройдет ли кирпич с ребрами  a, b, с  в прямоугольное отверстие со 
сторонами x и y. Просовывать кирпич в отверстие можно только так, чтобы 
каждое из его ребер было параллельно или перпендикулярно каждой  из 
сторон отверстия. 
"""

a,b,c,x,y = float(input()), float(input()), float(input()), float(input()), float(input())

if a<x and  (b<y or c<y) or a<y and (b<x or c<x) or b<x and (a<y or c<y) or b<y and (a<x or c<x) or c<x and (a<y or b<y) or c<y and (a<x or b<x):
    print('можно')
else:
    print('нельзя')