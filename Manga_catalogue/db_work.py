from os import path
import csv

from err_check import matching_rec, find_manga
from logg import logging

all_data = {}
last_id = 0
name_db = "Manga_catalogue.csv"


def read_all():
    global all_data, last_id

    logging.info(f"Show all manga. Database File - {name_db}")
    print(name_db)
    if path.exists(name_db):
        with open(name_db, "r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            all_data = [i for i in csv_reader]
            last_id = all_data[-1]["id"]
            return all_data
    else:
        logging.warning(f"Database not connected! Database file missing.")
        print("База данных не подключена!")


def print_all():
    for_output = [" ".join(k.values()) for k in all_data]
    print(*for_output, sep="\n", end=f"\n\n")


def add_manga(data):
    global last_id

    logging.info(f"Adding a new manga: {data}")

    if all(data.values()) and matching_rec(data, all_data):
        last_id = int(last_id) + 1
        data["id"] = last_id

        with open(name_db, "a", encoding="utf-8", newline="") as file:
            fieldnames = ["id", "manga", "genre", "year_issue", "status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(data)
            logging.warning(f"Data added in: {data.values()}")
            print("Данные добавлены\n")
    else:
        logging.warning(f"The data is already present in the database")
        print("Данные уже имеются в базе данных")


def del_manga(data_del):
    global all_data

    logging.info(f"Deleting manga: {data_del}")
    id_cand = find_manga(data_del, all_data)
    if id_cand:
        id_del = input(f"Введите id: ")
        logging.info(f"Id selected: {id_del}")

        if id_del in id_cand:
            all_data = [k for k in all_data if k["id"] != id_del]
            with open(name_db, "w", encoding="utf-8", newline="") as file:
                fieldnames = ["id", "manga", "genre", "year_issue", "status"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(all_data)
                logging.info(f"Data deleted")
                print("Данные удалены\n")
        else:
            logging.warning(f"No data found: {data_del}")
            print("Id не найден.\n")
    else:
        logging.warning(f"No data found: {data_del}")


def edit_manga(data_change, id_change):
    global all_data
    key, value = data_change

    logging.info(f"Data changes: {data_change}")
    if find_manga(id_change, all_data):
        for i, v in enumerate(all_data):
            if v["id"] == id_change:
                logging.info(f"Current value: {v[key]}")
                v[key] = value
                logging.info(f"New value: {v[key]}")
                all_data[i] = v

        with open(name_db, "w", encoding="utf-8", newline="") as file:
            fieldnames = ["id", "manga", "genre", "year_issue", "status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_data)
            logging.info(f"Data changed")
            print("Данные изменены\n")
    else:
        logging.warning(f"No data found: {data_change}")
        print("Id не найден.\n")


def file_import(name):
    global name_db

    logging.info(f"Changing the database file: {name}")
    if path.exists(name):
        name_db = name
        print(name_db)
    else:
        logging.warning(f"The database was not found: {name}")
        print("База данных не найдена.\n")


def save_csv(file_name):
    logging.info(f"Export in csv format: {file_name}.csv")

    with open(f'{file_name}.csv', 'w', encoding="utf-8", newline="") as file_w, \
            open('Manga_catalogue.csv', encoding="utf-8") as file_r:
        all_data = csv.DictReader(file_r)
        fieldnames = ["id", "manga", "genre", "year_issue", "status"]
        writer = csv.DictWriter(file_w, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_data)
        print(f"{file_name}.csv файл сохранен\n")
