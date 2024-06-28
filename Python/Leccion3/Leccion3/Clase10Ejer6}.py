def procesar_numeros(numeros):
    suma_pares = 0
    cantidad_pares = 0
    suma_impares = 0
    cantidad_impares = 0

    for num in numeros:
        if num % 2 == 0:
            suma_pares += num
            cantidad_pares += 1
        else:
            suma_impares += num
            cantidad_impares += 1

    promedio_impares = suma_impares / cantidad_impares if cantidad_impares > 0 else 0

    return suma_pares, cantidad_pares, promedio_impares

# solicitamos al usuario que ingrese la cantidad de numeros y los numeros
N = int(input("ingresa la cantidad de numeros: "))

numeros = []
for i in range(N):
    numero = int(input(f"ingresa el numero {i + 1}: "))
    numeros.append(numero)

# procesa los numeros y obtener resultados
suma_pares, cantidad_pares, promedio_impares = procesar_numeros(numeros)

# muestra los resultados
print(f"suma de los numeros pares: {suma_pares}")
print(f"cantidad de numeros pares: {cantidad_pares}")
print(f"promedio de los numeros impares: {promedio_impares}")