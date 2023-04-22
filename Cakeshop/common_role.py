import json


def documentation(filename: str) -> dict:
    """Функция чтения документации из JSON и создания в ее в виде словаря"""
    try:
        file = open(file=filename, mode='r')
        docs = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        file = open(file=filename, mode='w')
        docs = {}

    file.close()
    return docs


def show_production(production: dict) -> None:
    """Показывает продукцию кондитерской"""
    if production:
        for title in production.keys():
            print(f"""
Название: {title}
Состав: {production[title]['Состав']},
Цена: {production[title]['Цена']} руб.
Остаток: {production[title]['Остаток']} шт.
""")
    else:
        print('Извините на данный момент вся продукция закончилась.')


def load_statistic(date):
    """Выгружает статистику из файла"""
    data = documentation(f'statistics/{date}.json')
    if data:
        client_counter = data["количество клиентов"]
        shop_balance = data["прибыль"]
    else:
        client_counter = 0
        shop_balance = 0

    return client_counter, shop_balance
