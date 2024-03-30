def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    pesos=(money - expense) // 1
    centavos=(money-expense)%1
    print("Ingresar gasto:")
    print(f"{expense}")

    print("Dinero recibido")
    print(f"{money}")

    print("\nVuelto")
    print(f"{pesos}")
    print(f"{centavos}")
