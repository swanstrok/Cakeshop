def show_production(production: dict) -> None:
    """Показывает продукцию кондитерской"""
    if production:
        for title in production.keys():
            print(f"""
Название: {title}
Состав: {production[title]['Состав']},
Цена: {production[title]['Цена']} руб.
Остаток: {production[title]['Остаток']} шт.
""")
    else:
        print('Извините на данный момент вся продукция закончилась.')
