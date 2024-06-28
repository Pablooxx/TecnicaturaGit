def suma_numeros_formula(n):
    return n * (n + 1) // 2


def main():
    while True:
        # solicita al usuario ingresar el numero N
        n = int(input("ingrese un numero N para calcular la suma de los primeros N numeros: "))

        # calcula la suma usando la formula
        suma = suma_numeros_formula(n)

        # muestra el resultado
        print(f"la suma de los primeros {n} numeros es: {suma}")

        # pregunta al usuario si desea continuar o no
        continuar = input("¿desea calcular la suma para otro numero? (s/n): ").lower()
        if continuar != 's':
            print("oki doki, bye")
            break


if __name__ == "_main_":
    main()