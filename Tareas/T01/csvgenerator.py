"""
author: Hernan4444
"""
import random
import datetime as dt


###############
# Variables a editar
numero_de_orders = 100
simbolos_ = ["KAM", "SIM", "RIN", "WUB", "NEC", "RUP", "BAN"]
monedas = ["Kamas", "Simoleon", "Rings", "Wubba lubba dub dub", "nebcoins", "Rupees", "Banana"]
usuarios = [
    ["Florencia", "Barrios", "flobarrios"],
    ["Andrés", "Fernández", "andresfdezc"],
    ["Joaquín", "Tagle", "jtagle2"],
    ["Fernando", "Pieressa", "FernandoPieressa"],
    ["Stephanie", "Chau", "stephichau"],
    ["Benjamín", "Cárcamo", "fringlesinthestreet"],
    ["Sebastián", "Guerra", "sguerra2"],
    ["Enzo", "Tamburini", "entamburini"],
    ["Hugo", "Navarrete", "hanavarrete"],
    ["Hernán", "Valdivieso", "hernan4444"],
    ["Sebastián", "Cruz", "sebacruzd"],
    ["Ignacio", "Acevedo", "Iqacevedo"],
    ["Octavio", "Vera", "ofvera"],
    ["Raúl", "Álvarez", "KnowYourselves"],
    ["Isaac", "Carrera", "ifcarrera"],
    ["Vicente", "Juárez", "vijuarez"],
    ["Alejandro", "Kaminetzky", "akaminetzkyp"],
    ["Santiago", "Torres", "chapito96"],
    ["Camilo", "López", "cilopez"],
    ["Jose Manuel", "Larraín", "jnlarrain"],
    ["Felipe", "Quinteros", "fnquinteros"],
    ["Erick", "Romero", "egromero"],
    ["Nicolás", "Balbontín", "nfbalbontin"],
    ["Paula", "Salvo", "pcsalvo"],
    ["Jorge", "Riesco", "jorgeriesco"],
    ["Felipe", "Dominguez", "fdominguezclaro"],
    ["Jessica", "Hormazabal", "Arcoirisky"],
    ["Tanya", "Garrido", "tcgarrido"],
    ["Tomas", "Salvadores", "TomasSalvadores"],
    ["Gustavo", "Prudencio", "GustavPrudencio"]
]
##################


number_orders = [str(x) for x in range(numero_de_orders)]


def __generate_random_birthday():
    start_date = dt.date(1990, 1, 1)
    end_date = dt.date(1997, 12, 31)
    days = (end_date-start_date).days
    return str(start_date + dt.timedelta(days=random.randint(0, days)))


def __generate_random_date_and_match(start_date):
    end_date = dt.date(2017, 8, 12)
    days = (end_date-start_date).days
    start = random.randint(0, days//20 + 2)
    start_2 = random.randint(0, days//20 + 2)
    start_date_1 = start_date + dt.timedelta(days=start)
    start_date_2 = start_date + dt.timedelta(days=min(start, start_2))
    match_date = start_date + dt.timedelta(days=random.randint(max(start, start_2), days))
    return start_date_1, start_date_2, str(match_date)


def create_users():
    attribute = ["name: string", "lastname: string", "username: string",
                 "birthday: string", "orders: list"]

    for user in usuarios:
        user.append(__generate_random_birthday())
        number = random.randint(0, min(len(number_orders), 5))
        orders_user = random.sample(number_orders, number)
        for elem in orders_user:
            number_orders.remove(elem)
        orders_user = ":".join(orders_user)
        user.append(orders_user)

    random.shuffle(usuarios)

    usuarios.insert(0, attribute)
    name, lastname, username, birthday, orders_user = zip(*usuarios)
    users = [name, lastname, username, birthday, orders_user]
    random.shuffle(users)

    with open("users.csv", mode="w", encoding="UTF-8") as file:
        for element in zip(*users):
            print(";".join(element), file=file)


def create_currencies():
    currencies_attributes = ["name: string", "symbol: string"]
    currencies = [currencies_attributes]
    for simbolos, money in zip(simbolos_, monedas):
        currencies.append([money, simbolos])

    money, simbolos = zip(*currencies)
    currencies = [money, simbolos]
    random.shuffle(currencies)

    with open("Currencies.csv", mode="w", encoding="UTF-8") as file:
        for element in zip(*currencies):
            print(";".join(element), file=file)


def create_orders():

    orders_attribute = ["order_id: int", "date_created: string", "date_match: string",
                        "amount: float", "price: float", "type: string", "ticker: string"]

    orders = []
    i = 0
    date_created_2 = dt.date(1997, 1, 1)
    while i < len(number_orders):
        date_created_1, date_created_2, date_match = __generate_random_date_and_match(date_created_2)
        amount = str(round(random.uniform(1, 300), 1))
        price = str(round(random.uniform(1, 300), 1))
        type_ = random.choice(["ask", "bid"])
        ticker = "".join(random.sample(simbolos_, 2))

        auxiliar_bool = random.choice([True, False])

        if auxiliar_bool and i < len(number_orders) - 2:  # Si hay match
            orders.append([number_orders[i], str(date_created_1), date_match, amount, price, type_, ticker])
            if type_ == "ask":
                type_ = "bid"
            else:
                type_ = "ask"
            orders.append([number_orders[i + 1], str(date_created_2), date_match, amount, price, type_, ticker])
            i += 1
        else:
            orders.append([number_orders[i], str(date_created_1), "", amount, price, type_, ticker])
        i += 1

    random.shuffle(orders)
    orders.insert(0, orders_attribute)
    order_id, date_created, date_match, amount, price, type_, ticker = zip(*orders)
    orders = [order_id, date_created, date_match, amount, price, type_, ticker]
    random.shuffle(orders)

    with open("orders.csv", mode="w", encoding="UTF-8") as file:
        for element in zip(*orders):
            print(";".join(element), file=file)


def create_database():
    create_orders()
    create_users()
    create_currencies()


if __name__ == '__main__':
    create_orders()
    create_users()
    create_currencies()
