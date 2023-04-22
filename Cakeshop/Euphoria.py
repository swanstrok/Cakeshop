import json

from admin import *
from cateter import cateter
from client import *


def documentation(filename: str) -> dict:
    """Функция чтения документации из JSON и создания в ее в виде словаря"""
    try:
        file = open(file=filename, mode='r')
        docs = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        file = open(file=filename, mode='w')
        docs = {}

    file.close()
    return docs


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

        with open(file="production.json", mode="w") as f:  # Сохранение изменений продукции в файл
            json.dump(production, f, ensure_ascii=False)


def main(production: dict) -> None:
    print("Добро пожаловать в кондитерскую!")
    role_choice(production)
    print('До свидания!\n')


if __name__ == '__main__':
    while True:
        main(documentation('production.json'))
