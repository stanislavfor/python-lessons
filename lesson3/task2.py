# Задача 2. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

n = int(input("Введите длину списка: "))
a = list(map(int, input("Введите последовательность из N целых чисел: ").split()))
print("Исходный список N =", end =' ')
print(a)
k = int(input("Введите число K: "))
a = a[--k:] + a[:--k]
print("Получаем", end =' ')
print(a)