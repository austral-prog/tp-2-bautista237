def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    gasto=23.75
    print(f"{gasto}")
    print("Dinero recibido")
    recibido=100
    print(f"{recibido}")
    print(f"\nVuelto")
    print(f"\nPesos:")
    pesos = money - expense
    pesos_entero = int(pesos)
    print(pesos_entero)
    print("Centavos")
    print(f"{(money-expense)%1}")
