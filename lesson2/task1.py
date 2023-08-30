# Задача 1. По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input: 5
# Output: 120 

def factorial(num):
    fact = 1
    while num > 1:
        fact = fact * num
        num = num-1
    return fact

num = int(input('Введите число: '))
print (f'Факториал числа {num} равен {factorial(num)}')