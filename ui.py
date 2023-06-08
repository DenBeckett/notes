import os, platform
import datetime as dt


def main_menu():
    """ Главное меню программы """
    name_menu = "Главное меню\n"
    menu = [
        "Обработать заметки",
        "Прочитать заметки",
        "Найти заметку",
        "Удалить заметки",
        "Загрузить заметки из файла",
        "Выгрузить заметки в файл",
        "Выход",
    ]
    return selecting_item(menu, name_menu)


def menu_operation():
    """ Меню работы с заметкой """
    name_menu = "Меню работы с заметкой\n"
    menu = [
        "Создать заметку",
        "Изменить заметку",
        "Удалить заметку",
        "Назад"
    ]
    return selecting_item(menu, name_menu)


def menu_import():
    """ Меню работы с записью """
    name_menu = "Меню импорта\n"
    menu = [
        "Загрузить файл c заменой заметок",
        "Загрузить файл с добавлением заметок",
    ]
    return selecting_item(menu, name_menu)


def menu_export():
    """Модуль сохранения данных в файл"""
    name_menu = "Меню экспорта\n"
    menu = [
        "Сохранить все данные в файл",
        "Сохранить избранные данные в файл",
        "Назад"
    ]
    return selecting_item(menu, name_menu)


def selecting_item(date_menu, name_menu):
    """ Модуль обработки выбора меню """
    while True:
        try:
            print(name_menu)
            for item in enumerate(date_menu, 1):
                print(item[0], item[1])
            item_number = int(input("\nВыберите пункт меню: "))
            if 1 <= item_number <= len(date_menu):
                return item_number
            else:
                raise ValueError
        except ValueError:
            clear()
            print("Выберите правильный пункт меню\n")


def entry_record_data():
    """ Модуль ввода данных записи """
    header = input("\nВведите заголовок: ")
    text = input("Введите текст заметки: ")
    date_recording = dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(date_recording)
    record = [header, text, date_recording]
    return record


def up_del_user(data, operation):
    """ Выбор номера записи """
    while True:
        try:
            num = int(input(f"\nВведите номер записи для {operation}: "))
            if 0 < num <= len(data):
                return num
            else:
                raise ValueError
        except ValueError:
            print("Введите правильное число:")


def show_result(data):
    """ Функция вывода на экран """
    clear()
    if (len(data) > 0):
        print("Список заметок\n")
        for item in data:
            print(*item)
        print()
    else:
        print("Записи отсутсвуют\n")


def selecting_file():
    path = input("\nВведите имя файла: ")
    return path


def search_notes():
    serach = input("\nВведите фразу для поиска: ")
    return serach


def yes_no():
    name_menu = "Сохранить данные ?\n"
    menu = [
        "Да",
        "Нет",
    ]
    return selecting_item(menu, name_menu)

def clear():
   if platform.system() == 'Windows':
      os.system('cls')
   else:
      os.system('clear')