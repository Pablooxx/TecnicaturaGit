#Ejercicio 1: agenda telefonica
# hacer un programa que simule una agenda de contactos. Crar un
#Diccionario donde la clase sea el nombre del usuario y el valor
# sea el telefono, el progrma tendrá el siguiente menú de opciones:
# 1.Nuevo Contacto
# 2.Borrar contacto
# 3.Ver contactos existentes
# 4.Salir

agenda = {}
while True:
    print('\t .:menu:.')
    print('1. Nuevo Contacto')
    print('2. Borrar Contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')
    opcion = int(input('Digite una opción de menú: '))
    if opcion == 1:
        nombre = input("Digite el nombre del contacto: ")
        telefono = input('Digite el numero de telefono: ')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto agregado exitosamente!')
        else:
            print('Ese nombre de contacto ya existe')
    elif opcion == 2:
        nombre = input('Cual es nombre del contacto: ')
        if nombre in agenda:
            del(agenda[nombre])
            print('Se ha eliminado el contacto!')
        else:
            print('El contacto no existe en la agenda')
    elif opcion == 3:
        print('Agenda de Contactos')
        for clave, valor in agenda.items():
            print(f'Nombre: {clave}, telefono: {valor}')
    elif opcion == 4:
        print('Gracias por utilizar su agenda de contactos')
        break
    else:
        print('La opción no existe en el menú')
    print()