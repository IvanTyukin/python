"""
10) точка с координатами (x,y) принадлежит внутренней области 
треугольника с вершинами A(0,5), B(5,0) и C(1,0);
"""

x, y = float(input()), float(input())

a = (0 - x) * (0 - 5) - (5 - 0) * (5 - y)
b = (5 - x) * (0 - 0) - (1 - 5) * (0 - y)
c = (1 - x) * (5 - 0) - (0 - 1) * (0 - y)

print(a>=0 and b>=0 and c>=0 or a<=0 and b<=0 and c<=0)