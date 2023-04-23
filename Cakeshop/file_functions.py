import datetime
import json
import os


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


def push_statistic(stat: dict) -> None:
    """Загрузка статистики прибыли и количества клиентов за день в файл"""
    os.chdir('statistics')
    with open(file=f'{str(datetime.date.today())}.json', mode='w') as f:
        json.dump(stat, f, ensure_ascii=False)
    os.chdir('..')


def create_statistic(price: int) -> None:
    """Создание статистики"""
    client_counter, shop_balance = load_statistic(str(datetime.date.today()))
    # Внесение изменений в статистику кондитерской
    stat = dict()
    stat["количество клиентов"] = client_counter + 1
    stat["прибыль"] = shop_balance + price
    push_statistic(stat)


def load_client_purchases(phone, price):
    data = documentation('clients/Euphoria_clients.json')
    data[phone]['Сумма покупок'] += price

    with open(file='clients/Euphoria_clients.json', mode='w') as f:
        json.dump(data, f, ensure_ascii=False)
