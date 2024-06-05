'''
miVariable = 3
print(miVariable)
miVariable = "tres"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))  # x824
# las literales se escriben x123 (x mas los ultimos tres digitos)
print(id(y))  # x568
print(id(z))  # x888

# Types int, float, String, Bool

x = 10
print(x)
print(type(x))

x = 14.5
print(x)
print(type(x))

x = "Hola Alumnos"
print(x)
print(type(x))

x = True
print(x)
print(type(x))

x = False
print(x)
print(type(x))

# Manejo de Cadenas (String)
# Clase 3
MiGrupoFavorito = "Las Pastillas del Abuelo: "
caracteristicas = "La Mejor Banda de Rock Nacional"
print("Mi grupo favorito es:", MiGrupoFavorito, caracteristicas)

Numero1 = "7"
Numero2 = "8"
print(int(Numero1) + int(Numero2))

# Tipos Booleanos (Bool)
miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print("El resultado es Verdadero")
else:
    print("El resultado es Falso")

# Procesar la entrada del usuario
# Funcion Input
# resultado = input("Digite un número: ")  # Regresa un dato tipo string
# print(resultado)

# Conversión de la entrada de datos
# numero1 = int(input("Escribe el primer numero: "))
# numero2 = int(input("Escribe el segundo numero: "))
# resultado = numero1 + numero2
# print("El resultado de la suma es: ", resultado)

Clasificacion = int(input("Que tal estuvo tu día del 1 al 10?"))
print(Clasificacion)

# CLASE 4
operandoA = 8
operandoB = 5

suma = operandoA + operandoB
# print("El resultado de la suma: ", suma)
print(f'El resultado de la suma es: {suma}')

resta = operandoA - operandoB
print(f'El resultado de la resta es: {resta}')

multiplicacon = operandoA * operandoB
print(f'El resultado de la multiplicacion es: {multiplicacon}')

division = operandoA / operandoB
print(f'El resultado de la division es: {division}')
division = operandoA // operandoB
print(f'El resultado de la division(int) es: {division}')

modulo = operandoA % operandoB
print(f'El resultado de la division o residuo(modulo) es: {modulo}')

exponente = operandoA ** operandoB
print(f'El resultado del exponente es: {exponente}')
'''

"""
alto = int(input("Proporciona el alto del rectangulo: "))
ancho = int(input("Proporciona el ancho del rectangulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print('Area: ', area)
print('perimetro: ', perimetro)

miVariable3 = 10
print(miVariable3)

# Operadores de reasignacion
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

# miVariable3 = miVariable3 - 2
miVariable3 -= 2
print(miVariable3)

# miVariable3 = miVariable3 * 3
miVariable3 *= 3
print(miVariable3)

# miVariable3 = miVariable3 / 2
miVariable3 /= 2
print(miVariable3)
"""
'''
# Operadores de Comparacion
d = 4
b = 2
resultado = d == b # Comprobamos si son iguales
print(resultado)

# Operador Diferente

resultado = d != b
print(resultado)

# Operador Mayor que

resultado = d > b
print(resultado)

# Operador Menor que

resultado = d < b
print(resultado)

# operador menor o igual que
resultado = d <= b
print(resultado)

# Operador Mayor o Igual que
resultado = d >= b
print(resultado)

# Ejercicio 1 Clase 4 Python
a = int(input("Digite un número: "))
print(f'el residuo de la división es: {a % 2}')
if a % 2 == 0:
    print(f'el valor de a es: {a} es un número PAR')
else:
    print(f'El valor de a es {a} es un número IMPAR')
'''
"""
# Ejercicio 2
edadAdulto = 18
edadpersona = int(input("Digite su edad: "))

if edadpersona >= edadAdulto:
    print(f'Su edad es: {edadpersona} años, usted es mayor de edad')
else:
    print(f"Su edad es: {edadpersona} años, sos menor de edad")
"""

# Clase 5
"""
a = False
b = True
# Operador and
resultado = a and b
print(resultado)

# Operador or
resultado = a or b
print(resultado)

# Operador not
resultado = not a
print(resultado)
"""
# Ejercicio: Valor dentro de un rango
"""
valor = int(input("Digite un número dentro del rango 0 y 5: "))
valorMinimo = 0
ValorMaximo = 5
dentroRango = ( valor >= valorMinimo and valor <= ValorMaximo)
if dentroRango:
    print(f'El valor {valor} esta dentro del rango')
else:
    print(f'El valor {valor} no esta dentro del rango')
"""

# Ejercicio Operador Or, Operador not
"""
vacaiones = False
diadescanso = True
if not (vacaiones or diadescanso):
    print('Tiene Trabajo que hacer')
else:
    print('Puede Asistir al Juego')
"""
"""
# Ejercicio: Rango entre 20 y 30 años


edad = int (input("Digite su edad: "))
#veinte = edad >= 20 and edad < 30
#print(veinte)
#treinta = edad >= 30 and edad < 40
#print(treinta)

#if veinte or treinta :
if ( 20 <= edad < 30) or (30 >= edad < 40): # Sintaxis simplificada del operador and
#     if veinte:
    print('Estas dentro del rango de los (20\'0) a (30\'0) años')
#     elif treinta:
#       print('Estas dentro del rango de los (30\'0) años')
#     else:
#       print('No estas dentro del rango')
else:
    print('No estas dentro del rango de los (20\'0) a (30\'0) años ')
"""
"""
numero1 = int(input('Digite el valor para el numero1: '))
numero2 = int(input('Digite el valor para el numero2: '))
if numero1 > numero2:
    print('El numero 1 es mayor')
else:
    print('El numero 2 es mayor')
"""
# Clase 6

