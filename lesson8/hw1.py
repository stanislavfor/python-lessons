# Задача 1. Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.


def enter_second_name():
    return input("Введите фамилию абонента: ").title()

def enter_first_name():
    return input("Введите имя абонента: ").title()

def enter_family_name():
    return input("Введите отчество абонента: ").title()

def enter_phone_number():
    return input("Введите номер телефона: ")

def enter_address_number():
    return input("Введите адрес абонента: ").title()

def enter_data():
  surname = enter_second_name() 
  name = enter_first_name()      
  family = enter_family_name()  
  number = enter_phone_number()
  address = enter_address_number()
  with open(r'book.txt', 'a', encoding='utf-8') as file:
    file.write(f'- {surname} {name} {family},\n{number}, {address};\n\n')

def print_data():
  print("Контакты ->")
  with open(r'book.txt', 'r', encoding='utf-8') as file:
    print(file.read())    

def delete_data(): # Доработать
  print('Выберете поисковые данные записи: \n'
    '1. Фамилия,\n'
    '2. Имя,\n'
    '3. Отчество')  
  delete_line = input('и введите поисковые данные для удаления ВСЕЙ записи: ').title()  
  with open(r'book.txt', 'w+', encoding='utf-8') as file:
    data_lines = file.read().strip().split('\n\n')
    print(f"Запись удалена ->")
    for del_item in data_lines:
      delete_item = del_item.replace('-', ' ').split()
      if delete_line in delete_item:
        print(*delete_item, end="\n\n")                      
        file.write(delete_item)
        

def search_line():
  print('Выбертите вариант поиска: \n'
    '1. Фамилия,\n'
    '2. Имя,\n'
    '3. Отчество,\n'
    '4. Телефон,\n'
    '5. Адрес')
  # index = int(input('Введите вариант: ')) - 1
  searched = input('и введите поисковые данные: ').title()
  with open(r'book.txt', 'r', encoding='utf-8') as file:
    data = file.read().strip( ).split('\n\n')    
    print("Результат поиска ->")
    for item in data:
      new_item = item.replace('-', ' ').split()   
      # new_item = item.replace('\n', ' ').split()           
      if searched in new_item:               
        print(*new_item, end="\n\n")


def interface():
  cmd = 0
  while cmd != '5':
    print("Выберите действие: \n"
      "1. Добавить контакт\n"
      "2. Вывести все контакты\n"
      "3. Поиск контакта\n"
      "4. Удалить контакт\n"
      "5. Выход")
    cmd = input("Введите действие: ")
    while cmd not in ('1', '2', '3', '4', '5'):
      print('Некорректный ввод')
      cmd = input("Введите действие: ")
    match cmd:
      case '1':
          enter_data()
      case '2':
          print_data()
      case '3':
          search_line()
      case '4':
          delete_data()
      case '5':
          print('Всего доброго! ')

interface()
