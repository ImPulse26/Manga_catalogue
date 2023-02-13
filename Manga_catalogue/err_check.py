import logging


def find_manga(manga_find, all_info):
    logging.info(f"Search for an manga: {manga_find}")
    manga = [" ".join(i.values()) for i in all_info if manga_find in i.values()]
    if manga:
        logging.info(f"Search result: {manga}")
        print(*manga, sep="\n", end="\n\n")
        return [n[0] for n in manga]
    else:
        logging.warning(f"Manga NOT found: {manga_find}")
        print("Манга не найдена.\n")
        return 0


def matching_rec(new_manga: dict, all_info):
    value = list(new_manga.values())[1:]
    all_values = [list(k.values())[1:] for k in all_info]
    return value not in all_values


def check_new_manga(year):
    answer = input(f"Введите {year}: ")
    while True:
        if year in "manga genre status":
            if answer.isalpha():
                break
        if year == "year_issue":
            if answer.isdigit() and len(answer) == 4:
                break
        answer = input(f"Некорректные данные!\n"
                       f"Введите {year}: ")
    return answer
