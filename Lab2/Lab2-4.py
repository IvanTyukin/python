"""
4. Напишите программу, которая вводит целое число, не превышающее 100, 
и выводит его прописью, например, 21 «двадцать один».
"""

num = int(input())

arr1 = ['ноль','один','два','три','четыре','пять','шесть','семь','восемь','девять','десять','одиннадцать','двенадцать','тринадцать','четырнадцать','пятнадцать','шестнадцать','семнадцать','восемнадцать','девятнадцать']

arr2 = ['двадцать','тридцать','сорок','пятьдесят','шестьдесят','семдесят','восемдесят','девяносто']


if num<20:
    print(arr1[num])
else:
    if num % 10 != 0:
        print(arr2[num // 10 - 2] + ' ' + arr1[num % 10])
    else:
        print(arr2[num // 10 - 2])