def show_production(production: dict) -> None:
    """Показывает продукцию кондитерской"""
    for title, information in production.items():
        print(f"""
Название: {title}
Состав: {information[0]}
Цена: {information[1]} руб.
Остаток: {information[2]} шт.
""")
