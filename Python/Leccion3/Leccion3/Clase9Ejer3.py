def clasificar_numeros():
    # inicializa los contadores
    positivos = 0
    negativos = 0
    neutros = 0

    # lee 10 números
    for _ in range(10):
        numero = float(input("ingrese un numero: "))

        # clasifica los numero
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            neutros += 1

    # muestra los resultados
    print(f"numeros positivos: {positivos}")
    print(f"numeros negativos: {negativos}")
    print(f"numeros neutros: {neutros}")


if __name__ == "_main_":
    clasificar_numeros()