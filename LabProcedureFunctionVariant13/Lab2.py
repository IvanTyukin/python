"""
Перевести заданное в десятичной системе число a в двоичную систему, используя функцию перевода.
"""

def getBin(n):
    s = ''
    while n != 0:
        s = str(n % 2) + s
        n //= 2
    return int(s)

num = int(input())
binaryNum = getBin(num)
print(binaryNum)