import os
# path = os.path.join('lesson8', 'phone_book.txt')
path = os.path.abspath('phone_book.txt')

def enter_data():
    last_name = input("Введите фамилию: ")
    print()
    if last_name != "":
        first_name = input("Введите имя: ")
        middle_name = input("Введите отчество: ")
        phone_number = input("Введите номер телефона: ")
        address = input("Введите адрес: ")    
        with open(path, 'a', encoding='utf-8') as file:
            file.write(f'- {last_name} {first_name} {middle_name}, {phone_number}, {address};\n')
        print("Запись успешно добавлена.")     
        app_return()
    else:
        app_return()


def search_line():
    search_data = input("Введите фамилию или имя для поиска: ").title()    
    if len(search_data) > 0:
        print("Результат поиска:")
        with open(r'book.txt', 'r', encoding='utf-8') as file:
            data = file.read().strip( ).split('\n')                         
            for item in data:  
                new_item = item.replace(',', ' ').split()             
                print(new_item)
                print(type(new_item))
                app_return()
    else:
        print()
        app_return()    


def modify_data():
    term = input("Введите фамилию или имя записи, которую хотите изменить: ")
    results = search_line(term)
    if len(results) == 0:
        print("Запись не найдена.")
    elif len(results) == 1:
        last_name, entry = results[0]
        print("Найдена следующая запись:")
        print_entry(last_name, entry)
        field = input("Введите поле, которое хотите изменить (Фамилия, Имя, Отчество, Номер телефона): ")
        new_value = input("Введите новое значение: ")
        entry[field] = new_value
        print("Запись успешно изменена.")
        print_entry(last_name, entry)
    else:
        print("Найдено несколько записей:")
        for i, (last_name, entry) in enumerate(results):
            print(f"{i + 1}.")
            print_entry(last_name, entry)
        choice = int(input("Введите номер записи, которую хотите изменить: ")) - 1
        last_name, entry = results[choice]
        field = input("Введите поле, которое хотите изменить (Фамилия, Имя, Отчество, Номер телефона): ")
        new_value = input("Введите новое значение: ")
        entry[field] = new_value
        print("Запись успешно изменена.")
        print_entry(last_name, entry)


def delete_data():
    term = input("Введите фамилию или имя записи, которую хотите удалить: ")
    results = search_line(term)
    if len(results) == 0:
        print("Запись не найдена.")
    elif len(results) == 1:
        last_name, entry = results[0]
        print("Найдена следующая запись:")
        print_entry(last_name, entry)
        confirm = input("Вы уверены, что хотите удалить данную запись? (Да/Нет): ")
        if confirm.lower() == "да":
            del phone_book[last_name]
            print("Запись успешно удалена.")
            print()
    else:
        print("Найдено несколько записей:")
        for i, (last_name, entry) in enumerate(results):
            print(f"{i + 1}.")
            print_entry(last_name, entry)
        choice = int(input("Введите номер записи, которую хотите удалить: ")) - 1
        last_name, entry = results[choice]
        confirm = input("Вы уверены, что хотите удалить данную запись? (Да/Нет): ")
        if confirm.lower() == "да":
            del phone_book[last_name]
            print("Запись успешно удалена.")            
            print()


def print_entry(last_name, entry):
    print("Фамилия:", last_name)
    print("Имя:", entry["Имя"])
    print("Отчество:", entry["Отчество"])
    print("Номер телефона:", entry["Номер телефона"])


def print_data():
    with open(path, 'r', encoding='utf-8') as file:        
        data = file.read().strip( ).split('\n')    
    if len(data) > 1:
        print("Контакты: ")
        with open(path, 'r', encoding='utf-8') as file:
            print(file.read())                             
            app_return()                       
    else:
        print("Телефонный справочник пуст.") 
        print()       
        app_return() 

def interface():
    print("Выберите действие:")    
    print("1. Добавить запись")
    print("2. Поиск по фамилии или имени")
    print("3. Изменить запись")
    print("4. Удалить запись")
    print("5. Вывести все записи")
    print("6. Выйти")
    choice = input("Введите действие: ")    
    if choice == "1":
        enter_data()
    elif choice == "2":
        search_line()
    elif choice == "3":
        modify_data()
    elif choice == "4":
        delete_data()
    elif choice == "5":
        print_data()
    elif choice == "6":        
        print('Всего доброго! ')
    else:
        print("Неверный пункт меню.")


phone_book = "phone_book.txt"

def app_return():    
    inter = interface()
    inter.show()  

interface()
