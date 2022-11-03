"""
Дан файл, в каждой строке которого записаны числа. Найти среднее 
арифметическое всех чисел строки и результат вывести  в другой файл.
"""

Fin  = open("input1.txt")
Fout = open("output1.txt", "w")
lst = Fin.readlines()
for s in lst:
    avg = sum(map(int, s.split())) / len(s.split())
    Fout.write(str(avg)+"\n")
    
Fin.close()
Fout.close()