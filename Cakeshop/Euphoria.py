import datetime
import json
import os

import admin
import cateter
import client
import common_role

def push_statistic(stat: dict) -> None:
    """Загрузка статистики прибыли и количества клиентов за день в файл"""
    os.chdir('statistics')
    with open(file=f'{str(datetime.date.today())}.json', mode='w') as f:
        json.dump(stat, f, ensure_ascii=False)
    os.chdir('..')





def create_statistic(price: int) -> None:
    """Создание статистики"""
    client_counter, shop_balance = common_role.load_statistic(str(datetime.date.today()))
    # Внесение изменений в статистику кондитерской
    stat = dict()
    stat["количество клиентов"] = client_counter + 1
    stat["прибыль"] = shop_balance + price
    push_statistic(stat)


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
            client.client(production)

        elif role == '2' or role == 'администратор':
            role_choiced = True
            admin.admin(production)

        elif role == '3' or role == 'поставщик':
            role_choiced = True
            cateter.cateter(production)

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
        main(common_role.documentation('production.json'))
