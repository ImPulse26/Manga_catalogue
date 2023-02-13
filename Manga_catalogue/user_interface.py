from err_check import *
from db_work import *


def menu():
    while True:
        read_all()
        print(f"Каталог Манги\n")
        main_menu = input("1. Показать весь каталог\n"
                        "2. Поиск манги\n"
                        "3. Добавить мангу\n"
                        "4. Редактировать данные\n"
                        "5. Удалить мангу\n"
                        "6. Экспорт/Импорт\n"
                        "7. Выход\n")
        match main_menu:
            case "1":
                print_all()
            case "2":
                find_manga(input("Введите мангу(с заглавной буквы), жанр, год выпуска или статус: "), read_all())
            case "3":
                add_manga(add_menu())
            case "4":
                print_all()
                id_change = input(f"Введите id: ")
                if find_manga(id_change, read_all()) and (answer := edit_menu()):
                    edit_manga(answer, id_change)
            case "5":
                del_manga(input("Введите жанр или год выпуска: "))
            case "6":
                import_export_menu()
            case "7":
                logging.info("Stop program.\n")
                print("Работа программы завершена")
                break
            case _:
                logging.warning(f"Select incorrect item in main menu.")
                print("Некорректные данные, повторите попытку.")


def add_menu():
    logging.info('Start add menu')
    add_dict = {"id": "1", "manga": "", "genre": "", "year_issue": "", "status": ""}
    for i in add_dict:
        if i != "id":
            add_dict[i] = check_new_manga(i)
    logging.info('Stop edit menu')
    return add_dict


def edit_menu():
    add_dict = {"id": "1", "manga": "", "genre": "", "year_issue": "", "status": ""}
    logging.info('Start edit menu')
    while True:
        print("\nРедактировать:")
        change = input("1. Манга\n"
                       "2. Жанр\n"
                       "3. Год выпуска\n"
                       "4. Статус\n"
                       "5. Выход\n")

        match change:
            case "1" | "2" | "3" | "4":
                type_date = add_dict[change]
                return type_date, check_new_manga(type_date)
            case "5":
                logging.info('Exited the edit menu')
                return 0
            case _:
                logging.warning(f"Select incorrect item in edit menu.")
                print("Некорректные данные, повторите попытку.")


def import_export_menu():
    logging.info('Start import/export menu')
    while True:
        print("\nИмпорт\\Экспорт:")
        change = input("1. Импортировать файл\n"
                       "2. Экспортировать файл\n"
                       "3. Выход\n")
        match change:
            case "1":
                file_import(input(f"Введите название файла для загрузки базы: "))
                return
            case "2":
                save_csv(input("Введите имя нового файла для выгрузки базых: "))
                return
            case "3":
                logging.info('Exited the import/export menu')
                break
            case _:
                logging.warning(f"Select incorrect item in Import/export menu.")
                print("Некорректные данные, повторите попытку.")
