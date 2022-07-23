#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

#Пример:

#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k=5
str1 = ''
for i in range(k):
    if i == 0 : 
        kaef = random.randint(1,100) 
    else: 
        kaef = random.randint(0,100)
    if kaef>0:
        str1 = str1 +" + "
        if  kaef >1 : str1 = str1 + str(kaef)+ "*"
        str1 = str1 + "x"
        if k-1-i>=1:
            str1 = str1 + "^" + str(k-i)

kaef = random.randint(0,100)
if kaef >0: str1=str1 + " + " + str(kaef)
str1 = str1 + " = 0"
str2 = str1[3:]
print (str2)
file = open("test.txt", "w")
file.write(str2)
file.close()

