# Клиент приходит в кондитерскую. Он хочет приобрести один или несколько видов
# продукции, а также узнать её состав.
# Реализуйте кондитерскую.
# У вас есть словарь, где ключ – название продукции (торт, пирожное, маффин и
# т.д.). Значение – список, который содержит состав, цену (за 100гр) и кол-во (в
# граммах).
# Предложите выбор:
# 1. Если человек хочет посмотреть описание: название – описание
# 2. Если человек хочет посмотреть цену: название – цена.
# 3. Если человек хочет посмотреть количество: название – количество.
# 4. Всю информацию.
# 5. Приступить к покупке:
# С клавиатуры вводите название торта и его кол-во. n – выход из программы.
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном
# списке
# 6. До свидания
import copy
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


def adding(production: dict):
    """Добавление продуктов в кондитерскую"""
    count_of_goods = int(input("Введите количество привезенных позиций товаров: "))
    for i in range(count_of_goods):
        name = input("Наименование товара: ")
        quantity = int(input("Количество товара: "))
        if name in production:
            production[name][2] += quantity
    return production


def purchaice(production: dict):
    global price
    price = 0
    global prod
    prod = copy.deepcopy(production)
    global bill
    bill = dict()
    while True:
        choice_prod = input(
            "Введите название товара, если ничего не желаете то введите 'n': ").lower()
        if choice_prod == 'n' or choice_prod not in production:
            break
        choice_qti = int(input("Введите количество товара: "))
        if choice_qti > production[choice_prod][2]:
            print("У нас нет столько((")
            continue

        price += production[choice_prod][1] * choice_qti
        production[choice_prod][2] -= choice_qti
        bill[choice_prod] = [f"Куплено: {choice_qti}",
                             f"Стоимость: {production[choice_prod][1] * choice_qti}"]

    bill["итоговая цена"] = price


def bill_client():
    try:
        os.mkdir(str(datetime.date.today()))
    except FileExistsError:
        pass
    os.chdir(str(datetime.date.today()))
    with open(f'check №{client_counter}.json', 'w') as f:
        json.dump(bill, f, ensure_ascii=False)
    os.chdir('..')


def main(production):
    global shop_balance
    shop_balance = 0
    global client_counter
    print("Добро пожаловать в кондитерскую!")
    role_choice = input("Введите свою роль (покупатель/поставщик/администратор): ").lower()
    if role_choice == 'поставщик':
        adding(production)
    elif role_choice == 'администратор':
        print("""
        Выберите:
        1 - Для просмотра выручки;
        2 - Для изменения цены на товар;
        3 - Для добавления новой продукции в кондитерскую
        4 - Для удаления продукции с кондитерской
        """)
        admin_choice = input()
        if admin_choice == '1':
            print(f"Выручка магазина: {shop_balance}.")
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
        with open("prods.json", "w") as f:
            json.dump(production, f, ensure_ascii=False)

    elif role_choice == 'покупатель':
        global balance
        balance = random.randint(0, 5000)
        print(f"Мой баланс {balance}")
        while True:
            print(f"""
                    У вас на балансе: {balance}
                    Введите для выбора:
                    1. Если хотите посмотреть описание - "описание";
                    2. Если хотите посмотреть цену: - "цена";
                    3. Если хотите посмотреть количество: – "количество";
                    4. Если хотите посмотреть всю информацию - "информация".
                    5. Если хотите приступить к покупке - "покупка"
                    6. Если хотите выйти из магазина - "выход"  
                """)
            choice = input("Введите свой выбор:\n").lower()

            for key, value in production.items():
                if choice == "описание":
                    print(f"{key} : {value[0]}")
                elif choice == "цена":
                    print(f"{key} : {value[1]}")
                elif choice == "количество":
                    print(f"{key} : {value[2]}")
                elif choice == "информация":
                    print(f"{key} : {value}")
                elif choice == "покупка":
                    purchaice(production)
                    if price > balance:
                        print("У вас недостаточно денег.")
                        production = copy.deepcopy(prod)
                        choice_again = input("Хотите ли вы вернуться к покупкам?(да/нет)\n").lower()
                        if choice_again == 'да':
                            purchaice(production)
                        elif choice_again == 'нет':
                            break
                    else:
                        print(f"Ваш чек:")
                        bill_client()
                        balance -= price
                        client_counter += 1
                        shop_balance += price
                        with open("prods.json", "w") as f:
                            json.dump(production, f, ensure_ascii=False)
                        break

            if choice == "выход":
                break
    return production


client_counter = 0
while (time.time() - start_time) < max_time:
    print(client_counter)
    main(documentation('prods.json'))
