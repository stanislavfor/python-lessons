# Задача 1. Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input("Введите N кол-во элементов первого множества: "))
m = int(input("Введите N кол-во элементов второго множества: "))
array_x = {}
x = input("Введите элементы первого массива (через пробел): ")
array_x = sorted(set(x.split()))

array_y = {}
y = input("Введите элементы второго массива (через пробел): ")
array_y = sorted(set(y.split()))

intersection_set = list(set(array_x).intersection(set(array_y)))
intersection_set = " ".join(intersection_set)
print(intersection_set)


# Дополнительное решение с рандомными массивами
# from random import randint
# n = set(randint(1, 100) for i in range(int(input("Введите N кол-во элементов первого множества: "))))
# print(*n)
# m = set(randint(1, 100) for i in range(int(input("Введите M кол-во элементов второго множества: "))))
# print(*m)
# result = "".join(map(str, sorted(n.intersection(m))))
# print(result)