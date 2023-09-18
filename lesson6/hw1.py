# Задача 1.  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# # Первый вариант решения
# a1 = int(input("Первый элемент: "))
# d = int(input("Шаг: "))
# n = int(input("Количество элементов: "))
# c = [a1 + (i - 1) * d for i in range(1, n + 1)]
# print(*c)

# # Второй вариант решения
# numbers = input("Первый элемент списка, шаг, количество элементов \n(введите через пробел): ")
# numbers = list(map(int, numbers.split()))
# # res_array = [numbers[0] + (i - 1) * numbers[1] for i in range(1, numbers[2] + 1)]
# res_array = [numbers[0] + i * numbers[1] for i in range(numbers[2])]
# print(*res_array)



# Третий вариант решения
numbers = input("Первый элемент списка, шаг, количество элементов \n(введите через пробел): ")
numbers = list(map(int, numbers.split()))
print(*list(range(numbers[0], numbers[0] + numbers[1] * numbers[2] , numbers[1])))
# print()