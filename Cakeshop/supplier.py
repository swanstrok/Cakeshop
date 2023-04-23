def supplier(production: dict) -> None:
    """Роль поставщика. Добавление продуктов в кондитерскую"""
    while True:
        print("""
1 - Поставить продукцию в кондитерскую;
2 - Выход.
        """)

        supplier_choice = input("Ваш выбор: ").lower()

        if supplier_choice == '1' or supplier_choice == 'поставить':
            title = input("Введите название товара: ").capitalize()

            if title in production:
                quantity = int(input("Введите количество привезенного товара: "))
                production[title]['Остаток'] += quantity
                print(f'{title} в количестве {quantity} шт. успешно добавлен в кондитерскую.')
            else:
                print("Такой продукции в нашей кондитерской нет. Просим прощения.")
                continue

        elif supplier_choice == '2' or supplier_choice == 'выход':
            break
