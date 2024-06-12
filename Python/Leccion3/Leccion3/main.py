# Ciclo While (mientras o durante)
'''
contador = 0
while contador < 78:
    print('Ejecutamos nuestro ciclo while ', +contador)
    contador +=1
else:
    print('fin del ciclo while')
'''

'''
# Imprimir número del 0 al 5 con el ciclo while
maximo = 5
contador = 0
while contador <= maximo:
    print(contador)
    contador += 1

# Imprimir número del 5 al 1 con el ciclo while
minimo = 1
contador = 5
while contador >= minimo:
    print(contador)
    contador -= 1

# Ciclo For (Ciclo limitado a diferencia del while que es ilimitado)
cadena = 'hello'
for letra in cadena:
    print(letra)
else:
    print('fin del ciclo de for')
    
# Palabra reservada break
for letra in ('Alemania'):
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break
else:
    print('Fin del ciclo For')
'''
# Palabra reservada continue
for i in range(6):
    if i % 2 == 0:
        print(f'Valor: {i}')

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')