#Ejercicio 5: factorial de un número positivo
# hacer un programa para calcular el factorial de un número positivo

numero = int(input('Digite un numero: '))
while numero < 0:
    print("Error -> El numero tiene que ser positivo")
    numero = int(input("digite un numero: "))
factorial = 1
for i in range(1, numero+1):
    factorial *= i
print(f'\nEl factorial del numero {numero} ingresado es: {factorial}')