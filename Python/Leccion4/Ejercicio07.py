#Ejericio 7: Juego adivina el número
# Realizar un nuego para adivinar un número. Para ello se debe
# Generar un número aleatorio entre 1 - 100, y luego ir pidiendo
# números indicando "es Mayor" o "es menor" según sea mayor o menor
# y allí se debe mostrar el número de intentos

import random
print('\t.:Adivina el número:.')
aleatorio = random.randint(0, 100)#toma de 0 a 100 literal
contador = 0
while True:
    numero = int(input('Digite un número: '))
    contador += 1
    if numero > aleatorio:
        print('\tNo es el numero, digite un numero menor')
    elif numero < aleatorio:
        print('\tNo es el numero, digite un numero mayor')
    else:
        print(f'FELICIDADES, acabas de adivinar el número {aleatorio}')
        break
print(f'\tNúmero de intentos: {contador}')