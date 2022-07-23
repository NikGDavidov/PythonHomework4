#Даны два файла, в каждом из которых находится запись многочлена. 
#Задача - сформировать файл, содержащий сумму многочленов.

import random

def createFile(k, fileName:str):

    str1 = ''
    for i in range(k):
      if i == 0 : 
        kaef = random.randint(1,5) 
      else: 
        kaef = random.randint(0,5)
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
    file = open(fileName, "w")
    file.write(str2)
    file.close()

def readFile(fileName:str):
    str1=''
    with open(fileName, "r") as file:
     for line in file:
        str1 = line
    return str1

# создаем и записываем два файла с многочленами
fileName1 = "test1.txt"
fileName2 = "test2.txt"
createFile(5,fileName1)
createFile(3,fileName2)

# считываем из двух файлов в строки и записываем все в одну строку (чтоб ничего не потерять)
str1 = readFile(fileName1)
str2 = readFile(fileName2)
print(str1)
print(str2)
str3 = str1 + '+'+ str2

# разбиваем строку на список list подстрок (многочленов)
str3 = str3.replace(' ','').replace('=0','')
list = str3.split('+')
#print (list)

result='' # в эту строку записываем результат

temp = 0
i=0

# в цикле пробегаем по списку list - ищем и складываем х с одинаковыми степенями (флаг "is_x"), либо числа - флаг "no_x"  
while  i < len(list):
    flag ='is_x'
    j = i+1
    if list[i].find('x') == -1:
        flag = 'no_x'
        temp = int(list[i])
    else :
        if list [i][0]=="x" : temp = 1
        else : temp = int(list[i][:list[i].find('*')]) 
     
        
    while j < len(list):
        if flag == 'no_x' and  list[j].find('x') == -1: 
            temp  += int(list[j])
            del list[j]
        elif list[i][list[i].find('x')+1:] == list[j][list[j].find('x')+1:]:
            if list[j][0]=="x": temp +=1
            else: temp += int(list[j][:list[j].find('*')])          
            del list[j]
        
        j=j+1

    result += str(temp)
    if flag=="is_x": 
        if list[i][0]=="x": result += list[i][list[i].find('x'):]
        else: result += list[i][list[i].find('*'):]
      
    result += " + "
    #print (result)
    i=i+1
result = result [:-3]
result += " = 0"  
print(result)

file = open("result.txt", "w")
file.write(result)
file.close()           