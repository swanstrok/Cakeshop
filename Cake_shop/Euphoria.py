import datetime
import time
import os
import json
import random

max_time = 28800
start_time = time.time()


def documentation(filename: str):
    """Создание документации"""
    with open(filename) as f:
        production = json.load(f)

    return production


def registry():
    """Регистрация нового постоянного клиента"""
    os.chdir('clients')
    try:
        data = documentation('cake_clients.json')
    except json.decoder.JSONDecodeError:
        data = dict()

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


def bill_client(bill: dict):
    """Создание чека"""
    try:
        data = documentation(f'statistics/{str(datetime.date.today())}.json')
        client_counter = data["количество клиентов"]
    except FileNotFoundError:
        client_counter = 0

    os.chdir('bills')

    try:
        os.mkdir(str(datetime.date.today()))
    except FileExistsError:
        pass
    os.chdir(str(datetime.date.today()))

    with open(f'check №{client_counter}.json', 'w') as f:
        json.dump(bill, f, ensure_ascii=False)
    os.chdir('..')
    os.chdir('..')


def stats(stat: dict):
    """Создание статистики прибыли и количества клиентов за день"""
    os.chdir('statistics')
    with open(f'{str(datetime.date.today())}.json', 'w') as f:
        json.dump(stat, f, ensure_ascii=False)
    os.chdir('..')
    return stat


def adding(production: dict):
    """Добавление продуктов в кондитерскую. Поставка"""
    count_of_goods = int(input("Введите количество привезенных позиций товаров: "))

    for i in range(count_of_goods):
        name = input("Наименование товара: ")

        if name in production:
            quantity = int(input("Количество товара: "))
            production[name][2] += quantity
            with open("prods.json", "w") as f:
                json.dump(production, f, ensure_ascii=False)

        else:
            print("Такого товара нет")


def client_check():
    """Проверяем клиента на наличие в списке постоянных клиентов.
    Возвращаем скидку, в соответствии с количеством посещений кондитерской данным клиентом."""
    cake_client = input("Есть ли у вас наша карта постоянного клиента? (д/н): ").lower()
    discount = 0

    global client_phone
    client_phone = None

    if cake_client == 'д':
        try:
            data = documentation('clients/cake_clients.json')
            client_phone = input("Введите номер телефона: ")

            if client_phone in data:
                sum_of_purchaises = data[client_phone]["Сумма покупок"]
                if sum_of_purchaises >= 10000:
                    discount = 0.3
                elif sum_of_purchaises >= 5000:
                    discount = 0.15

                return discount

            else:
                print("Извините, но вас нет в списке наших постоянных клиентов.")
                while True:
                    our_client_choice = input("Не желаете ли приобрести карту? (д/н): ")
                    if our_client_choice == 'д':
                        registry()
                        break
                    elif our_client_choice == 'н':
                        break

        except json.decoder.JSONDecodeError:
            print("Извините, но вас нет в списке наших постоянных клиентов.")
            while True:
                our_client_choice = input("Не желаете ли приобрести карту? (д/н): ")
                if our_client_choice == 'д':
                    registry()
                    break
                elif our_client_choice == 'н':
                    break

    elif cake_client == 'н':
        while True:
            our_client_choice = input("Не желаете ли приобрести карту? (д/н): ")
            if our_client_choice == 'д':
                registry()
                break
            elif our_client_choice == 'н':
                break

    return discount


def purchaice(production: dict):
    """Процесс выбора товаров"""
    price = 0
    bill = dict()
    discount = client_check()

    while True:
        choice_prod = input(
            "Введите название товара, если ничего не желаете то введите 'n': ").lower()

        if choice_prod == 'n' or choice_prod not in production:
            break

        choice_qti = int(input("Введите количество товара: "))

        if choice_qti > production[choice_prod][2]:
            print("У нас нет столько((")
            continue

        price += production[choice_prod][1] * choice_qti * (1 - discount)
        production[choice_prod][2] -= choice_qti
        bill[choice_prod] = [f"Куплено: {choice_qti}",
                             f"Стоимость: {production[choice_prod][1] * choice_qti * (1 - discount)}",
                             f"Скидка: {discount * 100}%"]

    bill["итоговая цена"] = price
    return bill, price


def prod(production: dict, balance: int):
    """Процесс оплаты товаров"""
    bill, price = purchaice(production)

    if price > balance:
        print("У вас недостаточно денег.")
        choice_again = input("Хотите ли вы вернуться к покупкам?(да/нет)\n").lower()
        if choice_again == 'да':
            purchaice(production)
        elif choice_again == 'нет':
            client(production)
    else:
        try:
            data = documentation(f'statistics/{str(datetime.date.today())}.json')
            client_counter = data["количество клиентов"]
            shop_balance = data["прибыль"]
        except FileNotFoundError:
            client_counter = 0
            shop_balance = 0

        # Внесение изменений в статистику кондитерской
        client_counter += 1
        shop_balance += price
        stat = dict()
        stat["количество клиентов"] = client_counter
        stat["прибыль"] = shop_balance
        stats(stat)

        balance -= price

        print(f"Ваш чек:")
        for i, j in bill.items():
            print(f"{i} : {j}")
        bill_client(bill)

        with open("prods.json", "w") as f:
            json.dump(production, f, ensure_ascii=False)

        # Внесение изменений в количество приходов клиента
        if client_phone is not None:
            f = open("clients/cake_clients.json")
            data = json.load(f)
            f.close()

            data[client_phone]["Сумма покупок"] += price

            f = open("clients/cake_clients.json", "w")
            json.dump(data, f, ensure_ascii=False)
            f.close()

    return balance


def client(production: dict):
    """Приход клиента"""
    balance = random.randint(0, 5000)
    while True:
        print(f"""
Мой баланс: {balance}
Введите для выбора:
1. Если хотите посмотреть состав;
2. Если хотите посмотреть цену;
3. Если хотите посмотреть количество;
4. Если хотите посмотреть всю информацию;
5. Если хотите приступить к покупке;
6. Если хотите выйти из магазина.
""")
        choice = input("Введите свой выбор:\n").lower()

        for key, value in production.items():
            if choice == "1":
                print(f"{key} : {value[0]}")
            elif choice == "2":
                print(f"{key} : {value[1]}")
            elif choice == "3":
                print(f"{key} : {value[2]}")
            elif choice == "4":
                print(f"{key} : {value}")
            elif choice == "5":
                balance = prod(production, balance)
                break
        if choice == "6":
            break


def admin(production: dict):
    """Роль админа"""
    while True:
        print("""
Выберите:
1 - Для просмотра выручки и количества клиентов за день;
2 - Для изменения цены на товар;
3 - Для добавления новой продукции в кондитерскую;
4 - Для удаления продукции с кондитерской;
5 - Для просмотра списка постоянных клиентов;
6 - Для выхода.
""")

        admin_choice = input()
        if admin_choice == '1':
            date = input("Укажите дату в формате (гггг-мм-дд): ")

            try:
                data = documentation(f'statistics/{date}.json')
                client_counter = data["количество клиентов"]
                shop_balance = data["прибыль"]
            except FileNotFoundError:
                client_counter = 0
                shop_balance = 0

            if date <= str(datetime.date.today()):
                print(
                    f"Выручка магазина: {shop_balance}.\n"
                    f"Количество клиентов за день: {client_counter}.")

            else:
                print("Простите, введенная дата еще не наступила.")

        elif admin_choice == '2':
            good_choice = input("Введите название товара: ")
            if good_choice in production:
                price_choice = int(input("Введите новую цену на товар: "))
                production[good_choice][1] = price_choice
                print(production)

        elif admin_choice == '3':
            good_choice = input("Введите название товара: ")
            if good_choice not in production:
                sostav = input("Введите состав товара через запятую: ")
                cost = int(input("Введите желаемую цену на товар: "))
                production[good_choice] = [None, None, None]
                production[good_choice][0] = sostav
                production[good_choice][1] = cost
                production[good_choice][2] = 0
                print(production)

        elif admin_choice == '4':
            good_choice = input("Введите название товара: ")
            if good_choice in production:
                del production[good_choice]
                print(production)

        elif admin_choice == '5':
            os.chdir('clients')
            try:
                data = documentation('cake_clients.json')
            except json.decoder.JSONDecodeError:
                data = dict()

            for customer, information in data.items():
                print(customer, ":", information)

        elif admin_choice == '6':
            break

    with open("prods.json", "w") as f:
        json.dump(production, f, ensure_ascii=False)


def main(production: dict):
    print("Добро пожаловать в кондитерскую!")
    role_choice = input("Введите свою роль (покупатель/поставщик/администратор): ").lower()

    if role_choice == 'поставщик':
        adding(production)

    elif role_choice == 'администратор':
        admin(production)

    elif role_choice == 'покупатель':
        print(production)
        client(production)


while (time.time() - start_time) < max_time:
    main(documentation('prods.json'))
