# Задача 1. На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

c = 0

coins = list(input('Введите обозначение монет 0 или 1 (без пробела): '))
# print(type(coins))
for element in coins:
  if int(element) == 1:
    c = c + 1
print("Output: ", c, "-> ", " ".join(map(str, coins)))
print( )

# list = []
# for element in input("Введите обозначение монет 0 или 1 через пробел: ").split():
#   list.append(int(element))

# # print([type(element) for element in list])
# print("На столе Вы положили ряд монет -> ", " ".join(map(str, list)))

# for element in list:
#   if element == 1:
#     c = c + 1
 
# print("Количество монет, которые нужно перевернуть: ", c)
# print("Output: ", c, "-> ", " ".join(map(str, list)))
# print( )
