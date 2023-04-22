import random

from common_role import show_production


def client(production: dict):
    """Приход клиента"""
    balance = random.randint(0, 5000)  # Генерирует случайный баланс клиента
    while True:
        print(f"""
Мой баланс: {balance}
Введите для выбора:
1. Посмотреть продукцию кондитеской;
2. Приступить к покупке;
3. Выход.
""")
        choice = input("Введите свой выбор:\n").lower()

        if choice == "1":
            show_production(production)
        elif choice == "2":
            pass
        elif choice == "3":
            break
