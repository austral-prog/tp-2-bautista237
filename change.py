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
    print("Centavos:")
    centavos=((money - expense)%1)*100
    centavos_completo=int(centavos)
    print(centavos_completo)
