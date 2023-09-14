# Задача 2. В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai  ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним. 
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# 4 -> 1 2 3 4
# 9


bilberry = input("Введите количество ягод на каждом кусте (через пробел): ")
bilberry = list(map(int, bilberry.split()))
print(" ->", end = ' ')
print(*bilberry)
berries_sum = 0
berries = 0
maximum = 0
# for i in bilberry:
#   berries_sum = sum([bilberry[i-1], bilberry[1]], bilberry[((i+1) - len(bilberry))])
#   if berries_sum > berries:
#     berries = berries_sum
# print(berries)
for i in bilberry:
  maximum = max(bilberry)
  if maximum == bilberry[0]:
    berries = int(bilberry[0]) + int(bilberry[1]) + int(bilberry[-1])
  elif maximum == bilberry[len(bilberry)-1]:
    berries = int(bilberry[-2]) + int(bilberry[len(bilberry)-1]) + int(bilberry[0])
  else:
    berries = ([bilberry[i-1], bilberry[1]], bilberry[((i+1) - len(bilberry))])
print(berries)
print("Максимальное число =", berries, "ягод с трёх соседних кустов")


