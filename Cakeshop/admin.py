def add_product(production: dict) -> dict:
    """Добавляет новый товар в продукцию кондитерской"""
    new_good_title = input("Введите название нового товара: ").capitalize()
    if new_good_title not in production:
        ingredients = input("Введите состав товара через запятую: ")
        price = int(input("Введите желаемую цену на товар: "))
        production[new_good_title] = [None, None, None]
        production[new_good_title][0] = ingredients
        production[new_good_title][1] = price
        production[new_good_title][2] = 0
        print(f'Товар {new_good_title} успешно добавлен в продукцию кондитерской.')
    else:
        print('Такой товар уже есть в продукции кондитерской.')

    return production


def change_price(production: dict) -> dict:
    """Изменяет цену товара"""
    good_title = input("Введите название товара: ").capitalize()

    if good_title in production:
        new_price = int(input("Введите новую цену на товар: "))
        production[good_title][1] = new_price
        print(f'Цена на {good_title} изменена на {new_price}.')

    else:
        print('Товара с таким названием нет в нашей кондитерской.')

    return production


def good_operations(production: dict):
    """Операции с продукцией"""
    good_operations_menu = """
1 - Изменить цену на товар;
2 - Добавить новый товар в кондитерскую;
3 - Удалить товар из кондитерской;
4 - Выйти в предыдущее меню.
    """

    print(good_operations_menu)

    while True:
        admin_goods_choice = input("Ваш выбор: ").lower()

        if admin_goods_choice == '1' or admin_goods_choice == 'изменить':
            change_price(production)
        elif admin_goods_choice == '2' or admin_goods_choice == 'добавить':
            add_product(production)
        elif admin_goods_choice == '3' or admin_goods_choice == 'удалить':
            pass
        print(good_operations_menu)

        if admin_goods_choice == '4' or admin_goods_choice == 'выйти':
            break


def admin(production: dict) -> None:
    """Роль админа"""
    while True:
        print("""
Выберите:
1 - Просмотр выручки и количества клиентов за день;
2 - Операции с продукцией;
3 - Просмотр списка постоянных клиентов;
4 - Выход.
""")
        admin_choice = input("Ваш выбор: ")

        if admin_choice == '1':
            pass

        elif admin_choice == '2':
            good_operations(production)

        elif admin_choice == '3':
            pass

        elif admin_choice == '4':
            break
