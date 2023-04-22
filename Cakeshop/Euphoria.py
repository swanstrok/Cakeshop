import json


def create_documentation(filename: str):
    """Функция чтения документации из JSON и создания в объекте Python"""
    with open(filename) as f:
        documentation = json.load(f)

    return documentation


def main():
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
    main()
