#Ejercicio 6: Tabla de multiplicar
# Hacer un programa que pida un número por teclado y guarde
# en una lista su tabla de multiplicar el 10. Por Ej:
# Si digita el 5 la lista tendrá: 5, 10, 15, 20, 25, 30, 40, 45, 50

numero = int(input('Digite un numero: '))
lista = []
for i in range (1, 11):
    lista.append(i * numero)

print(f'\nTabla de multiplicar del {numero}: \n {lista}')
for indice, i in enumerate(lista):
    print(f'{numero} * {i} = {lista[indice]}')
