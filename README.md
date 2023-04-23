# Euphoria Cakeshop
___
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django)


**Euphoria Cakeshop** - this project represents a cakeshop based on Python Core. This is a test 
project without connecting to databases and using frameworks. All your data saves in json-files.

## Usage
You can choose one of the suggested roles (administrator, customer, supplier) and try to participate
in the work of our cakeshop.

### Administrator
Administrator can:
- view daily statistics, which shows the number of customers per day and the daily 
revenue of the cakeshop;
- perform various operations with products (add products the cakeshop, change
its price, delete products from cakeshop or view the production of cakeshop); 
- view the list of regular customers.

```python
def admin(production: dict) -> None:
    """Роль админа"""
    while True:
        print("""
Выберите:
1 - Просмотр выручки и количества клиентов за день;
2 - Операции с продукцией;
3 - Просмотр списка постоянных клиентов;
4 - Выход.
""")
        admin_choice = input("Ваш выбор: ")
```

### Client
Client has a random amount of money. He/She can:
- view the cakeshop production;
- buy production of cakeshop; 
- register in cakeshop loyality program to get discounts based on his/her purchase price. 

```python
import random

def client(production: dict) -> None:
    """Приход клиента"""
    costs = 0
    balance = random.randint(0, 5000)  # Генерирует случайный баланс клиента
    while True:
        print(f"""
Мой баланс: {balance}
Введите для выбора:
1. Посмотреть продукцию кондитеской;
2. Приступить к покупке;
3. Выход.
""")
        choice = input("Введите свой выбор: ").lower()
```

### Supplier
Supplier can add production to our cakeshop.

```python
def supplier(production: dict) -> None:
    """Роль поставщика. Добавление продуктов в кондитерскую"""
    while True:
        print("""
1 - Поставить продукцию в кондитерскую;
2 - Выход.
        """)

        supplier_choice = input("Ваш выбор: ").lower()
```

