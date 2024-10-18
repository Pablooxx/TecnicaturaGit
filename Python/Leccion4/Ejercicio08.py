#Ejercicio 8: Menú interactivo - Cajero automatico
# Hacer un programa que simule un cajero automatico con saldo
# inicial de $1000 y tendrá el siguiente menú de opciones:
# 1. Ingresar dinero en la cuenta
# 2. Retirar dinero de la cuenta
# 3. Mostrar dinero disponible
# 4. Salir

saldo = 1000
while True:
    print('\t.:MENU:.')
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero en la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")
    opcion = int(input("digite una opcion del menú: "))
    print()
    if opcion == 1:
        extra = float(input("Cuanto dinero desa ingresar -> "))
        saldo += extra
        print(f'Dinero en la cuenta al momento: ${saldo}')
    elif opcion == 2:
        retirar = float(input("Cuanto dinero desea retirar -> "))
        if retirar > saldo:
            print("No tiene saldo suficiente")
        else:
            saldo -= retirar
            print(f'Dinero en la cuenta al momento: ${saldo}')

    elif opcion == 3:
        print(f'Dinero en la cuenta al momento: ${saldo}')

    elif opcion == 4:
        print('Gracias por utilizar su cajero automatico, hasta pronto')
        break
    else:
        print('Esto es un error, se equivoco de opción')
        print()