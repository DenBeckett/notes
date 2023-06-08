import csv


def file_csv_import(path):
    lst = []
    try:
        with open(f"{path}.csv", "r", encoding="utf8") as file:
            file_csv = csv.reader(file, delimiter=";", lineterminator="\r")
            for row in file_csv:
                lst.append(row)
            lst_new = []
            for item in lst:
                lst = list(item)
                del lst[0]
                item = tuple(lst)
                lst_new.append(item)
            return tuple(lst_new)
    except FileNotFoundError:
        print("Файл не существует")
        return lst


def file_csv_export(data, name_file):
    with open(f"{name_file}.csv", "w", encoding="utf8") as file:
        file_csv = csv.writer(file, delimiter=";", lineterminator="\r")
        file_csv.writerows(data)