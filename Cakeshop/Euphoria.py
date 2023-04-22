import json


def documentation(filename: str) -> dict:
    """Функция чтения документации из JSON и создания в ее в виде словаря"""
    # with open(filename) as f:
    #     docs = json.load(f)

    try:
        file = open(file=filename, mode='r')
        docs = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        file = open(file=filename, mode='w')
        docs = {}

    file.close()

    return docs


def admin(production: dict) -> None:
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
        admin_choice = input("Ваш выбор: ")

        if admin_choice == '1':
            pass

        elif admin_choice == '2':
            pass

        elif admin_choice == '3':
            pass

        elif admin_choice == '4':
            pass

        elif admin_choice == '5':
            pass

        elif admin_choice == '6':
            break


def client(production: dict) -> None:
    """Роль покупателя"""
    pass


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
                    json.dump(production, f, ensure_ascii=True)
            else:
                print("Такой продукции в нашей кондитерской нет. Просим прощения.")
                continue

        elif cateter_choice == '2' or cateter_choice == 'выход':
            break


def role_choice(production: dict) -> None:
    """Функция выбора роли"""
    role_choiced = False

    while not role_choiced:
        print("""
Выберите свою роль:
        
1 - Покупатель;
2 - Администратор;
3 - Поставщик;
4 - Выход.
""")

        role = input("Ваш выбор: ").lower()

        if role == '1' or role == 'покупатель':
            role_choiced = True
            print('Привет, покупатель!')
            client(production)

        elif role == '2' or role == 'администратор':
            role_choiced = True
            print('Привет, администратор!')
            admin(production)

        elif role == '3' or role == 'поставщик':
            role_choiced = True
            print('Привет, поставщик!')
            cateter(production)

        elif role == '4' or role == 'выход':
            break

        else:
            role_choiced = False
            print("Простите, такой роли в нашей кондитерской не предусмотрено.")


def main(production: dict) -> None:
    print("Добро пожаловать в кондитерскую!")
    role_choice(production)
    print('До свидания!\n')


if __name__ == '__main__':
    while True:
        main(documentation('production.json'))
