# Задача 2. Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

# A = -5 9 0 3 -1 -2 1 4 -2 10 2 0 -9 8 10 -9 0 -5 -5 7

# array_num = input("Введите элементы массива (через пробел): ")
# array_num = list(map(int, array_num.split()))
# # print(array_num)
# min_num = int(input("Первый элемент: "))
# max_num = int(input("Последний элемент: "))
# if max_num >= min_num:
#   print("Вывод: ", end = ' ')
#   for i in range(len(array_num)):
#     if min_num <= array_num[i] <= max_num:
#       print(i, end = ' ')


# Вариант с генератором списка:
array_num = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
array_num = [a for a in array_num]
print("Ввод: ", end = ' ')
print(*array_num)
min_num = int(input("Первый элемент: "))
max_num = int(input("Последний элемент: "))
if max_num >= min_num:
  print("Вывод: ", end = ' ')
  for i in range(len(array_num)):
     if min_num <= array_num[i] <= max_num:
       print(i, end = ' ')
  
