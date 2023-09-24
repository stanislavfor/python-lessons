# Задача 1. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле. 
# 1. Программа должна выводить данные.
# 2. Программа должна сохранять данные в текстовом файле.
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной.

import os
path_root = os.path.join('lesson8', 'book.txt')


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
    with open(path_root, 'a', encoding='utf-8') as file:
        file.write(f'{surname} {name} {family}, {number}, {address}\n')

def print_data():
    with open(path_root, 'r', encoding='utf-8') as file:
        print(file.read())


def search_line():
    print('Выбертите вариант поиска:\n'
          '1. Фамилия\n'
          '2. Имя\n'
          '3. Отчество\n'
          '4. Телефон\n'
          '5. Адрес')
    index = int(input('Введите вариант: ')) - 1
    searched = input('Введите поисковые данные: ').title()
    with open(path_root, 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
        for item in data:
            new_item = item.replace('\n', ' ').split()
            if searched in new_item[index]:
                print(new_item.read(), end="\n\n")
        # file.seek(0)
        # print(file.readlines())

def interface():
    cmd = 0
    while cmd != '4':
        print("Выберите действие: \n"
              "1. Добавить контакт\n"
              "2. Вывести все контакты\n"
              "3. Поиск контакта\n"
              "4. Выход\n")
        cmd = input("Введите действие: ")
        while cmd not in ('1', '2', '3', '4'):
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
                print('Всего доброго! ')

interface()