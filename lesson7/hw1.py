# Задача 1. Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.
# Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывод: Парам пам-пам

# text = "пара-ра-рам рам-пам-папам па-ра-па-дам"
def poem(): 
  vowels =  'ауоыийэяюёе'
  poem_string = text.split()
  vowels_sum = [] 
  for phrase in poem_string:
    s = 0 
    for letter in phrase:      
      if letter in vowels:
        s += 1
    vowels_sum.append(s)  
# return len(vowels_sum) == list.count(vowels_sum[0])    
  if vowels_sum[1:] != vowels_sum[:-1]:
    print('vowels =', vowels_sum, "-> ", end = " ")
    return "Пам парам" 
  print('vowels =', vowels_sum, "-> ", end = " ")
  return "Парам пам-пам"     
text = input("Введите стихотворение Винни-Пуха: ")
print(poem())



# # Пример решения задачи:
# def vowels_f(letters):
#     vowels = 'ауоыийэяюёе'
#     count = 0
#     for letter in letters:
#       if letter.lower() in vowels:
#         count += 1
#     return count
# def check_f(text):
#     print(text.capitalize(), end = " ")
#     phrases = text.split(" ")
#     style = []
#     for phrase in phrases:
#       words = phrase.split("-")
#       rows = []
#       for letters in words:
#           row_count = vowels_f(letters)
#           rows.append(row_count)
#       style.append(rows)
#     for i in range(1, len(style)):
#       if style[i] != style[i-1]:
#         return "= Парам пам-пам"
#     return "= Пам парам"
# text = input("Введите текст стихотворения, где\nслова отделены дефисами, а фразы отделены пробелами: ")
# print(check_f(text))



# Пример решения задачи из урока:
# def sum_vowels(phrase):
#   vowels_letters ='ауоыийэяюёе'
#   k = 0
#   for letter in phrase:
#     if letter in vowels_letters:
#       k += 1
#   return k
# def pam_param(phrases):
#   sum_0 = sum_vowels(phrases[0])
#   for phrase_i in phrases[1:]:
#     sum_i = sum_vowels(phrase_i)
#     if sum_0 != sum_i:
#       return "Пам парам"
#   return "Парам пам-пам"
# text = input("Введите текст песни Винни-Пуха: ").split()
# print(pam_param(text))



