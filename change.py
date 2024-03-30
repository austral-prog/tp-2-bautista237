def change():
    expense = 23.75
    money = 100
    print(f"Ingresar gasto:\n{expense}")
    print(f"Dinero recibido\n{money}")
    print(f'Vuelto\n\nPesos:\n{(money - expense) // 1}\nCentavos:\n{(money-expense)%1}')
