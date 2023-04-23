import json
import random

from file_functions import show_production, create_statistic, documentation, load_client_purchases


def authentication(phone: str, data) -> bool:
    """Аутентификация пользователя"""
    if phone in data:
        return True
    return False


def registration(phone, data):
    """Регистрация нового постоянного клиента"""
    name = input("Введите ваше имя: ")
    surname = input("Введите вашу фамилию: ")
    email = input("Введите ваш email: ")
    information = dict()
    information["Имя"] = name
    information["Фамилия"] = surname
    information["Email"] = email
    information["Сумма покупок"] = 0
    data[phone] = information

    with open('clients/Euphoria_clients.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False)

    print("Регистрация успешно пройдена.")
    return phone


def non_authorized_offer(data):
    """Предложение для неавторизованных пользователей стать постоянным клиентом"""
    while True:
        our_client_choice = input("Не желаете ли приобрести карту? (д/н): ")
        if our_client_choice == 'д':
            phone = input("Введите ваш номер телефона: ")
            if authentication(phone, data):
                print("Извините пользователь с таким номером телефона уже существует.")
                return authorization()
            return registration(phone, data)
        elif our_client_choice == 'н':
            return None


def authorization() -> tuple:
    """Авторизируем пользователя"""
    discount = 0
    phone = None
    data = documentation('clients/Euphoria_clients.json')
    euphoria_client = input("Есть ли у вас наша карта постоянного клиента? (д/н): ").lower()

    if euphoria_client == 'д':
        phone = input("Введите ваш номер телефона: ")

        if authentication(phone, data):
            sum_of_purchaises = data[phone]["Сумма покупок"]
            if sum_of_purchaises >= 10000:
                discount = 0.3
            elif sum_of_purchaises >= 5000:
                discount = 0.15

        else:
            print("Извините, но вас нет в списке наших постоянных клиентов.")
            phone = non_authorized_offer(data)
    elif euphoria_client == 'н':
        phone = non_authorized_offer(data)

    return discount, phone


def order_create(production: dict):
    """Процесс формирования заказа"""
    price = 0
    order = dict()
    discount, phone = authorization()

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

        cost = production[good_title]['Цена'] * quantity * (1 - discount)
        order[good_title] = {
            'Количество': quantity,
            'Цена за 1 шт.': production[good_title]['Цена'],
            'Скидка': f'{discount * 100}%',
            'Общая стоимость:': cost
        }
        price += cost
        print(order)
    return order, price, phone


def balance_check(balance: int, price: int) -> bool:
    """Проверка на наличие у покупателя нужной суммы денег"""
    if price > balance:
        print("У вас недостаточно денег.")
        return False
    else:
        return True




def purchaise(production: dict, balance: int, costs: int):
    """Процесс оплаты товаров"""
    order, price, phone = order_create(production)

    if order:
        if balance_check(balance, price):
            balance -= price
            costs += price
            for good in order.keys():
                production[good]['Остаток'] -= order[good]['Количество']

            if phone is not None:
                load_client_purchases(phone, costs)

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
