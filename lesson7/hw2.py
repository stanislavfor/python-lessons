# Задача 2. Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
# Ввод: 
# print_operation_table(lambda x, y: x * y)
# Вывод:
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36


# Первый вариант
def print_operation_table(operation, num_rows=6, num_columns=6):
  for row in range(1, num_rows + 1):
    for col in range(1, num_columns + 1):      
      print(*[f"{operation(row, col):>3}"], end = "")
    print("\n", end = "")
print_operation_table(lambda x, y: x * y)


# Второй вариант
# def print_operation_table(operation, num_rows=6, num_columns=6):
#   table = "" 
#   for row in range(1, num_rows+1):        
#     for col in range(1, num_columns+1):
#       table += f"{operation(row, col)} "
#     table += "\n"
#   print(table)
# print_operation_table(lambda x, y: x * y) 



# Пример решения задачи:
# def print_operation_table(operation, num_rows=6, num_columns=6):  
#   table = [[operation(row, col) for col in range(1, num_columns + 1)] for row in range(1, num_rows + 1)]
#   for row in table:
#     print(*[f"{x:>3}" for x in row])
# print_operation_table(lambda x, y: x * y)


