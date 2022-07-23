#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# 1) решение через множество
# list1 = list(map(int, input("Введите числа через пробел:\n").split()))
# st =set()
# for i in list1:
#     st.add(i)
# listUnic = list(st) #если нужен именно тип list (список)
# print(f'{list1} -> {listUnic}')

# 2) решение через список
list1 = list(map(int, input("Введите числа через пробел:\n").split()))
listUnic = []
[listUnic.append(i) for i in list1 if i not in listUnic]
print(f'{list1} -> {listUnic}')