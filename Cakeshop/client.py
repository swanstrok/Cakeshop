import json
import os
import random

from file_functions import show_production, create_statistic, documentation


def registry():
    """Регистрация нового постоянного клиента"""
    os.chdir('clients')
    data = documentation('Euphoria_clients.json')
    phone = input("Введите ваш номер телефона: ")

    if phone in data:
        print("Извините, пользователь с таким номером телефона уже существует.")

    else:
        name = input("Введите ваше имя: ")
        surname = input("Введите вашу фамилию: ")
        email = input("Введите ваш email: ")
        information = dict()
        information["Имя"] = name
        information["Фамилия"] = surname
        information["Email"] = email
        information["Сумма покупок"] = 0
        data[phone] = information

        with open('cake_clients.json', 'w') as f:
            json.dump(data, f, ensure_ascii=False)

        print("Регистрация успешно пройдена.")

    os.chdir('..')


def order_create(production: dict):
    """Процесс формирования заказа"""
    price = 0
    order = dict()

    while True:
        good_title = input(
            "Введите название товара, если ничего не желаете то введите '-': ").capitalize()

        if good_title == '-':
            break

        elif good_title not in production:
            print("У нас нет товара с таким названием.")
            continue

        quantity = int(input("Введите количество товара: "))

        if quantity > production[good_title]['Остаток']:
            print("Извините, но у нас нет такого количества.")
            continue

        cost = production[good_title]['Цена'] * quantity
        order[good_title] = {
            'Количество': quantity,
            'Цена за 1 шт.': production[good_title]['Цена'],
            'Итого': cost
        }
        price += cost

    return order, price


def balance_check(balance: int, price: int) -> bool:
    """Проверка на наличие у покупателя нужной суммы денег"""
    if price > balance:
        print("У вас недостаточно денег.")
        return False
    else:
        return True


def purchaise(production: dict, balance: int, costs: int):
    """Процесс оплаты товаров"""
    order, price = order_create(production)

    if order:
        if balance_check(balance, price):
            balance -= price
            costs += price
            for good in order.keys():
                production[good]['Остаток'] -= order[good]['Количество']

        else:
            choice_again = input("Хотите ли вы вернуться к покупкам?(да/нет): ").lower()
            if choice_again == 'да':
                return purchaise(production, balance, costs)
            elif choice_again == 'нет':
                return client(production)

    return balance, costs


def client(production: dict) -> None:
    """Приход клиента"""
    costs = 0
    balance = random.randint(0, 5000)  # Генерирует случайный баланс клиента
    while True:
        print(f"""
Мой баланс: {balance}
Введите для выбора:
1. Посмотреть продукцию кондитеской;
2. Приступить к покупке;
3. Выход.
""")
        choice = input("Введите свой выбор: ").lower()

        if choice == "1":
            show_production(production)
        elif choice == "2":
            balance, costs = purchaise(production, balance, costs)
        elif choice == "3":
            if costs:
                create_statistic(costs)
            break
