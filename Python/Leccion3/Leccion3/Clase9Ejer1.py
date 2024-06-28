def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False


def main():
    while True:
        # solicita al usuario ingresar un año
        anio = int(input("Ingrese un año para verificar si es bisiesto: "))

        # verifica si el año es bisiesto
        if es_bisiesto(anio):
            print(f"el año {anio} es bisiesto.")
        else:
            print(f"el año {anio} no es bisiesto.")

        # pregunta al usuario si desea continuar o no
        continuar = input("¿deseas verificar otro año? (s/n): ").lower()
        if continuar != 's':
            print("bye bye")
            break


# se ejecuta la funcion principal
if __name__ == "_main_":
    main()