# Задача 2. Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6
# Чи́сла Фибона́ччи — элементы числовой последовательности:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946,…
# Последовательность Фибоначчи определяется так: φ(0)=0, φ(1)=1, ..., φn=φ(n-1) + φ(n-2).


def fibonacci(num):
  a = 0
  b = 1
  i = 1
  while a <= num:
    if num == a:
      return i
      break
    a = b
    b = a + b
    i = + 1
  else:
    return(-1)




num = int(input("Введите натуральное число A большее 1: "))
# if a > 1:
#   def fibonacci(a):
#     a_0 = 0
#     a_1 = 1
#     i = 1
#     while a_0 <= a:
#       if a == a_0:
#         return i  
#         break  
#       a_0 = a_1     
#       a_1 = a_0 + a_1          
#       i =+ 1  
#     else:
#       # print("А не является числом Фибоначчи.", end = ' ')
#       # print(-1)   
#       return (-1)
# else:
#   print("Введите натуральное число A большее 1. Ошибка.")

print(fibonacci(num))