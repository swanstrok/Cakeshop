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


def admin(production: dict):
    """Роль админа"""
    pass


def client(production: dict):
    """Роль покупателя"""
    pass


def cateter(production: dict):
    """Роль поставщика"""
    pass


def main(production: dict):
    print("""
Добро пожаловать в кондитерскую!

Выберите свою роль:
    
1 - Покупатель;
2 - Администратор;
3 - Поставщик
""")

    role_choice = input("Ваш выбор: ").lower()

    if role_choice == '1' or role_choice == 'покупатель':
        print('Привет, покупатель!')
        client(production)

    elif role_choice == '2' or role_choice == 'администратор':
        print('Привет, администратор!')
        admin(production)

    elif role_choice == '3' or role_choice == 'поставщик':
        print('Привет, поставщик!')
        cateter(production)


if __name__ == '__main__':
    main(documentation('production.json'))
