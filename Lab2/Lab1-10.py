"""
10. Определить, является ли шестизначное число "счастливым" (сумма 
первых трех цифр равна сумме последних трех цифр).
"""

a = input()

if len(a) == 6 and int(a[0]) + int(a[1]) + int(a[2]) == int(a[3]) + int(a[4]) + int(a[5]):
    print('является')
else:
    print('не является')