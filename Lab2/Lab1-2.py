"""
2. Дано пятизначное число. Определить, упорядочены ли по возрастанию 
цифры в записи числа. Например, 13789 цифры упорядочены по 
возрастанию. А в числе 34609 – нет.
"""

i = int(input())

s= str(i)
if len(s) == 5 and s[0]<=s[1]<=s[2]<=s[3]<=s[4]:
    print('цифры упорядочены по возрастанию')
else:
    print('цифры не упорядочены по возрастанию')