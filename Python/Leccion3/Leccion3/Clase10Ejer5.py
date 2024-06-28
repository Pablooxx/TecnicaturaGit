def factorial(n):
    if n < 0:
        raise ValueError("el numero debe ser mayor o igual a 0")
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

# solicitamos al usuario que ingrese un numero
numero = int(input("ingresa un numero mayor o igual a 0: "))

# calcula el factorial y mostrar el resultado
try:
    print(f"el factorial de {numero} es {factorial(numero)}")
except ValueError as e:
    print(e)