import json
import os
import time
import datetime
import random

max_time = 28800
start_time = time.time()
shop_balance = 0
client_counter = 0


class LoadAndSave:
    """Загрузка и сохранение файлов"""

    def __init__(self):
        try:
            self.stat = self.load_documentation(f'statistics/{str(datetime.date.today())}.json')
        except FileNotFoundError:
            self.stat = {"количество клиентов": 0,
                         "прибыль": 0}

    def load_documentation(self, filename: str):
        """Загрузка документации"""
        with open(filename) as f:
            self.production = json.load(f)

        return self.production

    def write_documentation(self, filename: str, file: str):
        """Внесение изменений в документацию"""
        with open(filename, "w") as f:
            json.dump(file, f, ensure_ascii=False)

    def stats(self, statistic):
        """Создание статистики прибыли и количества клиентов за день"""
        os.chdir('statistics')
        with open(f'{str(datetime.date.today())}.json', 'w') as f:
            json.dump(statistic, f, ensure_ascii=False)
        os.chdir('..')
        return self.stat


class Sale:
    """Класс для продажи продукции"""

    def __init__(self):
        self.files = LoadAndSave()
        self.production = self.files.load_documentation('prods.json')
        self.stat = self.files.stat
        self.shop_balance = self.stat["прибыль"]
        self.client_counter = self.stat["количество клиентов"]

    def purchaice(self):
        """Процесс выбора товаров"""
        self.price = 0
        while True:
            self.choice_prod = input(
                "Введите название товара, если ничего не желаете то введите 'n': ").lower()
            if self.choice_prod == 'n' or self.choice_prod not in self.production:
                break
            self.choice_qti = int(input("Введите количество товара: "))
            if self.choice_qti > self.production[self.choice_prod][2]:
                print("У нас нет столько((")
                continue

            self.price += self.production[self.choice_prod][1] * self.choice_qti
            self.production[self.choice_prod][2] -= self.choice_qti

        return self.price

    def prod(self, balance):
        """Процесс оплаты товаров"""
        print(f"Мой баланс {balance}")
        self.price = self.purchaice()
        if self.price > balance:
            print("У вас недостаточно денег.")
            self.choice_again = input("Хотите ли вы вернуться к покупкам?(да/нет)\n").lower()
            if self.choice_again == 'да':
                self.purchaice()
            # elif self.choice_again == 'нет':
            #     self.client(production)
        else:
            self.client_counter += 1
            self.shop_balance += self.price
            self.files.write_documentation("prods.json", self.production)
            # with open("prods.json", "w") as f:
            #     json.dump(self.production, f, ensure_ascii=False)
        self.stat["количество клиентов"] = self.client_counter
        self.stat["прибыль"] = self.shop_balance
        self.files.stats(self.stat)
        return self.price


class Client:
    """Класс клиента"""

    def __init__(self):
        self.balance = random.randint(0, 5000)
        self.sale = Sale()

    def client(self):
        """Приход клиента"""
        print("Добро пожаловать в Euphoria!")
        while True:
            print("""
    Введите для выбора:
    1. Если хотите посмотреть описание;
    2. Если хотите посмотреть цену;
    3. Если хотите посмотреть количество;
    4. Если хотите посмотреть всю информацию;
    5. Если хотите приступить к покупке;
    6. Если хотите выйти из магазина.
    """)
            self.choice = input("Введите свой выбор:\n").lower()

            for key, value in self.sale.production.items():
                if self.choice == "1":
                    print(f"{key} : {value[0]}")
                elif self.choice == "2":
                    print(f"{key} : {value[1]}")
                elif self.choice == "3":
                    print(f"{key} : {value[2]}")
                elif self.choice == "4":
                    print(f"{key} : {value}")
                elif self.choice == "5":
                    self.balance -= self.sale.prod(self.balance)
                    print(self.balance)
                    break

            if self.choice == "6":
                print("До свидания!")
                break


class Cakeshop:
    """Класс работы кондитерской"""

    def role_choice(self):
        self.role = input("Введите свою роль (покупатель/поставщик/администратор): ").lower()
        if self.role == 'поставщик':
            pass
        elif self.role == 'администратор':
            pass
        elif self.role == 'покупатель':
            c = Client()
            c.client()


cs = Cakeshop()
while (time.time() - start_time) < max_time:
    cs.role_choice()
