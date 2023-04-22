import json


def cateter(production: dict) -> None:
    """Роль поставщика. Добавление продуктов в кондитерскую"""
    while True:
        print("""
1 - Поставить продукцию в кондитерскую;
2 - Выход.
        """)

        cateter_choice = input("Ваш выбор: ").lower()

        if cateter_choice == '1' or cateter_choice == 'поставить':
            title = input("Введите название товара: ")

            if title in production:
                quantity = int(input("Введите количество привезенного товара: "))
                production[title][2] += quantity
                with open(file='production.json', mode='w') as f:
                    json.dump(production, f, ensure_ascii=False)
            else:
                print("Такой продукции в нашей кондитерской нет. Просим прощения.")
                continue

        elif cateter_choice == '2' or cateter_choice == 'выход':
            break
