# Задача 1. Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# 5
# 1 2 3 4 5
# 3
# -> 1
import random

n = int(input("Укажите N количество элементов в массиве : "))
a = []
for i in range(n):
    a[i] = random.randint(1, 100)

count = 0
x = int(input("Укажите число X : "))

for i in range(n):
    if a[i] == x:
        count += 1

print("Количество повторений числа X в массиве ->", count)  
