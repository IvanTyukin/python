"""
3. Напишите программу, которая вводит номер месяца и выводит название 
времени года. При вводе неверного номера месяца должно быть выведено 
сообщение об ошибке.
"""

months=['jan', 'feb', 'mar', 'apr', 'may', 'june', 'july', 'aug', 'sept', 'oct', 'nov', 'dec']

num = int(input())

if 1 <=num <= 12:
    print(months[num - 1])
else:
    print('not existed number of month')