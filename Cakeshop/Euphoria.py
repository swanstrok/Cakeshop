import json


def documentation(filename: str) -> dict:
    """Функция чтения документации из JSON и создания в ее в виде словаря"""
    with open(filename) as f:
        docs = json.load(f)

    return docs


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

    elif role_choice == '2' or role_choice == 'администратор':
        print('Привет, администратор!')

    elif role_choice == '3' or role_choice == 'поставщик':
        print('Привет, поставщик!')


if __name__ == '__main__':
    try:
        production = documentation('production.json')
    except FileNotFoundError:
        production = open(file='production.json', mode='w')
        production.close()
    main(production)
