"""
1. Тестовые задания последовательно вывести на экран, ввести номер 
правильного ответа и получить оценку. Тестовые задания:
Запишите номер правильного, на Ваш взгляд, ответа:
Вопрос 1. Система программного обеспечения, что управляет работой всех 
структурных узлов компьютера, называется: 1 автоматизированная, балл=0; 
2 операционная, балл=2; 3 интеллектуальная, балл=0.
Вопрос 2. Совокупность данных, что размещены на диске и имеют общее 
имя и назначение – это: 1 файл, балл=2 ; 2 процессор, балл=0; 3 сектор, 
балл=0;
Вопрос 3. Для изображения в блок-схеме алгоритма условия разветвления 
используются графические элементы: 1 квадрат, балл=0; 2 круг, балл=0; 3 
ромб, балл=1.
"""

question1='''Вопрос 1. Система программного обеспечения, что управляет работой всех 
структурных узлов компьютера, называется: 1 автоматизированная, балл=0; 
2 операционная, балл=2; 3 интеллектуальная, балл=0.'''
question2='''Вопрос 2. Совокупность данных, что размещены на диске и имеют общее 
имя и назначение – это: 1 файл, балл=2 ; 2 процессор, балл=0; 3 сектор, 
балл=0;'''
question3='''Вопрос 3. Для изображения в блок-схеме алгоритма условия разветвления 
используются графические элементы: 1 квадрат, балл=0; 2 круг, балл=0; 3 
ромб, балл=1.'''

print(question1)
a = int(input())
if a==1 or a==3:
    print('0 баллов')
elif a==2:
    print('2 балла')
    
print(question2)
b = int(input())
if b==2 or b==3:
    print('0 баллов')
elif b==1:
    print('2 балла')
    
print(question3)
c = int(input())
if c==1 or c==2:
    print('0 баллов')
elif c==3:
    print('1 балл')