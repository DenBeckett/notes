import sqlite3 as sql

TABLE_NAME = "list_notes"


connect = sql.connect("db_note.db")
cursor = connect.cursor()


def create_table():
    cursor.execute(f""" CREATE TABLE IF NOT EXISTS {TABLE_NAME}(
    id              INTEGER        PRIMARY KEY AUTOINCREMENT,
    header          VARCHAR(50),
    text            TEXT,
    date_recording  DATE 
    );
    """)


create_table()


def insert_one_entry_db(data):  # Добавление одной записи
    cursor.execute(
        f"INSERT INTO {TABLE_NAME} (header, text, date_recording) VALUES(?, ?, ?);", data
    )
    connect.commit()


def insert_db(data):  # Добавление нескольких записей
    try:
        query = f"""INSERT INTO {TABLE_NAME}
                (header, text, date_recording) VALUES(?, ?, ?);"""
        if len(data) > 1:
            cursor.executemany(query, data)
        else:
            cursor.execute(query, data[0])
    except sql.ProgrammingError:
        print("Не верный формат данных")
    connect.commit()


def update_one_entry_db(num, data):  # Заменить одну запись
    update_query = f""" UPDATE {TABLE_NAME} set header = ?, text = ?, date_recording = ? WHERE id = ?; """
    data_query = [data[0], data[1], data[2], num]
    cursor.execute(update_query, data_query)
    connect.commit()


def delete_db():  # Очистить таблицу полностью
    cursor.execute(f"DROP TABLE {TABLE_NAME};")
    create_table()
    connect.commit()


def delete_one_entry(num):  # Удалить одну запись таблицы
    cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = {num};")
    three_results = read_db()
    lst_new = []
    for item in three_results:
        lst = list(item)
        del lst[0]
        item = tuple(lst)
        lst_new.append(item)
    delete_db()
    insert_db(lst_new)
    connect.commit()


def read_db():
    cursor.execute(f"SELECT * FROM {TABLE_NAME};")
    data = cursor.fetchall()
    connect.commit()
    return data


def search_db(search):
    cursor.execute(
        f"SELECT * FROM {TABLE_NAME} WHERE header LIKE '%{search}%'")
    data = cursor.fetchall()
    connect.commit()
    return data