"""Создать текстовый файл с произвольной информацией. Организовать 
просмотр содержимого файла  «Человек»: фамилия; имя; отчество; пол; 
национальность; рост; вес; дата рождения (год, месяц число); номер 
телефона; домашний адрес (почтовый индекс, страна, область, район, 
город, улица, дом, квартира). Вывести сведения о самом молодом 
человеке.Организовать чтение и обработку данных из файла в 
соответствии с индивидуальным заданием. Сохранить полученные 
результаты в новый текстовый файл."""

Fin  = open("input2.txt")
Fout = open("output2.txt", "w")

lst = Fin.readlines()
year = 2022
month = 10
day = 26
smax = Fin.readline()

for s in lst:
    arr = s.split(",")
    if int(arr[7].strip()) < year:
        smax = s
        year = int(arr[7].strip())
        month = int(arr[8].strip())
        day = int(arr[9].strip())
    else:
        if int(arr[8].strip())<month:
            smax = s
            year = int(arr[7].strip())
            month = int(arr[8].strip())
            day = int(arr[9].strip())
        else:
            if int(arr[9].strip())<day:
                smax = s
                year = int(arr[7].strip())
                month = int(arr[8].strip())
                day = int(arr[9].strip())
Fout.write(smax+"\n")
Fin.close()
Fout.close()