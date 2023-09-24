# Задача 1. Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.

import os
path = os.path.join('lesson8', 'notes_book.txt')
# path = os.path.abspath('notes_book.txt')

def add_contact():
  surname = input("Введите фамилию: ")
  name = input("Введите имя: ")
  middle_name = input("Введите отчество: ")
  phone = input("Введите номер телефона: ")
  address = input("Введите адрес: ")
  with open(path, "a", encoding='utf-8') as file:
    file.write(f"{surname}, {name}, {middle_name}, {phone}, {address} \n")
    

def print_contacts(): 
  print("Телефонная книга, Контакты: ") 
  with open(path, "r", encoding='utf-8') as file:
    for line in file:       
      print(line.strip())

            
def search_contacts():
  search_query = input("Введите имя или фамилию для поиска: ")
  print("Телефонная книга, Результат поиска:") 
  with open(path, "r", encoding='utf-8') as file:
    for line in file:
      if search_query.lower() in line.lower():         
        print(line.strip())


def update_contact():
  surname = input("Введите фамилию записи, которую нужно изменить: ")    
  print("Вы собираетесь изменить контакт: ")
  with open(path, "r", encoding='utf-8') as file:
    for line in file:
      if surname.lower() in line.lower():
        print(line.strip())
  new_surname = input("Введите новую фамилию: ")
  new_name = input("Введите новое имя: ")
  new_middle_name = input("Введите новое отчество: ")
  new_phone = input("Введите новый номер телефона: ")
  new_address = input("Введите новый адрес: ")
  with open(path, "r+", encoding='utf-8') as file:
    lines = file.readlines()
    file.seek(0)
    for line in lines:      
      if surname.lower() in line.lower():
        file.write(f"{new_surname}, {new_name}, {new_middle_name}, {new_phone}, {new_address} \n")
        print("Контакт изменен успешно")
      else:
        file.write(line)
    file.truncate()


def delete_contact():
  surname = input("Введите фамилию записи, которую нужно удалить: ")
  name = input("Введите имя записи, которую нужно удалить: ")
  with open(path, "r+", encoding='utf-8') as file:
    for line in file:        
      print(f'Контакт: {line.strip()} - удален')
    lines = file.readlines()
    file.seek(0)      
    for line in lines:
      if surname.lower() not in line.lower() or name.lower() not in line.lower():
        file.write(line)        
    file.truncate()


def import_contacts():  
  import_file_path = input("Введите путь к файлу (имя файла) для импорта: ")
  with open(import_file_path, "r", encoding='utf-8') as import_file:
    with open(path, "a", encoding='utf-8') as file:
      for line in import_file:
        file.write(line)


def export_contacts():
  export_file_path = input("Введите путь к файлу (имя файла) для экспорта: ")
  with open(path, "r", encoding='utf-8') as file:
    with open(export_file_path, "w", encoding='utf-8') as export_file:
      for line in file:
        export_file.write(line)


def interface():
  choice = 0
  while choice != '8':
    print("Телефонная книга, Меню:")    
    print("1. Добавить запись")
    print("2. Поиск по фамилии или имени")
    print("3. Изменить запись")
    print("4. Удалить запись")     
    print("5. Экспортировать данные в файл")
    print("6. Импортировать данные из файла")
    print("7. Вывести все записи")
    print("8. Выйти")
    choice = input("Выберите пункт меню: ") 
    if choice == "1":
      add_contact()
    elif choice == "2":
      search_contacts()
    elif choice == "3":
      update_contact()
    elif choice == "4":
      delete_contact()  
    elif choice == "5":      
      export_contacts()    
    elif choice == "6":      
      import_contacts()  
    elif choice == "7":
      print_contacts()  
    elif choice == "8":
      print('Всего доброго! ')
    else:
      print("Неверный пункт меню.")


# path = "notes_book.txt"
# def app_return():    
#     inter = interface()
#     inter.show() 

interface()