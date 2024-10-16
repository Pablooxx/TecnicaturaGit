#Ejercicio 3: insertar elementos y ordenarlos
#pedir números y meterlos en una lista, cuando el usuario
#introduzca un numero 0, nuestro programa dejaría de insertar
#por ultimo, mostrar los número ordenados de menor a mayor

lista = []
salir = False
while not salir:
    numero = int(input('Digite un numero: '))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort()#la lista ordenada con esta funcion
print(f'\nLista odenada: \n{lista}')