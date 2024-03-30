def earth():
    X = "Bangladesh"
    Y = "Barbados"
    resultado_X_antes_Y = cmp(X, Y) < 0
    resultado_Y_antes_X = cmp(Y, X) < 0
    print(f"El resultado de {X} viene primero en el diccionario que {Y} es {resultado_X_antes_Y}")
    print(f"El resultado de {Y} viene primero en el diccionario que {X} es {resultado_Y_antes_X}")
