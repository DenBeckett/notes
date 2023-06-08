import ui, db, exp_imp


def run():
    """Модуль запуска программы"""
    ui.clear()
    while True:
        select_main_menu = ui.main_menu()
        if select_main_menu == 1:
            ui.clear()
            select_record_processing(ui.menu_operation())
        elif select_main_menu == 2:
            ui.show_result(db.read_db())
        elif select_main_menu == 3:
            ui.clear()
            serch_db = db.search_db(ui.search_notes())
            ui.show_result(serch_db)
        elif select_main_menu == 4:
            ui.clear()
            db.delete_db()
            print("Все записи удалены\n")
        elif select_main_menu == 5:  # Загрузить
            ui.clear()
            processing_import_menu(
                ui.menu_import(),
                ui.selecting_file().split(".")
            )
            ui.clear()
            print("База данных обновлена успешно\n")
        elif select_main_menu == 6:  # Выгрузить
            ui.clear()
            export_file(ui.menu_export())
        else:
            exit()


def select_record_processing(item):
    """ Обработка меню работы с записью """
    if item == 1:
        data = ui.entry_record_data()
        db.insert_one_entry_db(data)
        ui.clear()
        print("Запись добавлена\n")
    elif item == 2:
        ui.clear()
        ui.show_result(db.read_db())
        if (len(db.read_db()) > 0):
            db.update_one_entry_db(
                ui.up_del_user(db.read_db(), "изменения"),
                ui.entry_record_data()
            )
            ui.clear()
            print("Запись изменена\n")
    elif item == 3:
        ui.clear()
        ui.show_result(db.read_db())
        if (len(db.read_db()) > 0):
            db.delete_one_entry(ui.up_del_user(db.read_db(), "удаление"))
        ui.clear()
        print("Запись удалена\n")
    else:
        run()


def export_file(item):
    """Модуль сохранения данных в файл"""
    if item == 1:
        data_db = db.read_db()
        exp_imp.file_csv_export(data_db, ui.selecting_file())
        ui.clear()
        print("Файл сохранен успешно\n")
    elif item == 2:
        ui.clear()
        serch_db = db.search_db(ui.search_notes())
        ui.show_result(serch_db)
        item_yes_no = ui.yes_no()
        if item_yes_no == 1:
            exp_imp.file_csv_export(serch_db, ui.selecting_file())
            ui.clear()
            print("Файл сохранен успешно\n")
        else:
            run()
    else:
        run()


def processing_import_menu(menu, path):
    """ Обработка меню импорта """
    try:
        data = exp_imp.file_csv_import(path[0])
        if menu == 1:
            db.delete_db()
            db.insert_db(data)
        else:
            db.insert_db(data)
    except IndexError:
        print("Неправильное имя файла")