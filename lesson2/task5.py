# Задача 5. Орел и Решка: Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
# Формат входных данных
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
# Формат выходных данных
# Программа должна вывести наибольшее количество подряд выпавших Решек.
# Примечание. Если выпавших Решек нет, то необходимо вывести число 0
# 0.
# Тестовые данные
# Sample Input 1:
# ОРРОРОРООРРРО
# Sample Output 1:
# 3
# Sample Input 2:
# ООООООРРРОРОРРРРРРР
# Sample Output 2:
# 7
# Sample Input 3:
# ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР
# Sample Output 3:
# 31


s=input("Введите текст, состоящий из букв русского алфавита 'О' и 'Р': ")
temp = 0
while "Р"*(temp+1) in s:
    temp+=1
if temp!=0:
    print("Наибольшее количество Решек, выпавших подряд ->", end =' ')
    print(temp)
else:
    print(0)