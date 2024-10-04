# Lista, Ariel, Erwing, Pablo, Nataliam Osvaldo
#Colecciones en Python

# A las listas es lo que se conoce en otros lenguajes como arreglos o vectores
#
nombres = ["Naty", "Osvaldo", "Pablo", "Er"]
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])
print(nombres[0:2]) # Solo muestra las posiciones del indice 0, 1 pero no el indice 2
# Ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ : 3]) # infices a mostrar 0, 1, 2
# Desde el indice indicado hasta el final
print(nombres[1: ])
#modificamos un valor
nombres[3] = "Erwing"
nombres[0] = "Natalia"
print(nombres)
#Iterar una lista
for nombre in nombres: # nombre es singular, la lista es plural
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")

# Preguntamos cuantos elementos tiene
print(len(nombres)) #Les pasamos como parametro la lista, nos dice cuantos elementos tiene la lista

#Agregamos un elemento
nombres.append("Marcelo") #la funcion append agrega un elemento
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(10)
print(nombres)

# Insertar un elemento en un indice especifico
nombres.insert(1,"Alberto")
print(nombres)
nombres.insert(3,"Debora")
print(nombres)

#Eliminamos un elemento
nombres.remove("Osvaldo")
print(nombres)

#Eliminar el último elemento
nombres.pop()
print(nombres)
#Eliminamos un indice especifico
del nombres[1]
print(nombres)
#Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

#Eliminar la lista
del nombres
#print(nombres)

# Definir una tupla
cocina = ('cuchara', 'Cuchillo', 'Tenedor')
print(len(cocina))

#Acceder a un elemetno, para esto utilizamos corchetes no parentesis
print(cocina[0])

#Mostramos de manera inversa
print(cocina[-1])

#Acceder a un rango
print(cocina[0:2])
#Ejemplo
Verduras = ('papa',) # Una tupla necesita aunque sea un elemento: la coma
#de lo contrario solo sería un tipo String: cadena

#Recorremos los elementos de la tupla
for cocinar in cocina: # Print esta usando \n para saltos de lineas
     print(cocinar, end=' ') # usamos end= para eliminar los saltos de lineas

cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print("\n", cocina)

#del cocina para eliminar la tupla
#print(cocina)

# tipo Set

planetas = {"marte", "jupiter","venus"}
print(len(planetas)) #usamos la funcion len - length

#Revisar si un elemento existe dentro de set
print("marte" in planetas)

#agregar un elemento
planetas.add("Tierra")#add es una función para agregar
print(planetas)

#Eliminar elentos, puede arrojar un error si el elemento no existe
planetas.remove("jupiter")#esta función ante un mal ingreso u inexistencia del elemento da error
print(planetas)
planetas.discard("Tierra")
print(planetas)

# Lipiar Set
planetas.clear()
print(planetas)
#del planetas
#print(planetas)

# "Maradona": 10 un diccionario esta compuesto por 2 elementos
#LLave y un Valor
# dict (ket, value)
diccionario = {
    'IDE': 'Integrated Development Enviroment',
    'POD': 'Programación Orientada a Objetos',
    'SARD': 'Sistema de Administración de Base de Datos'
}
print(len(diccionario))
print(diccionario)

#Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

#otra forma
print(diccionario.get('POD'))
print(diccionario.get('SARD'))

#Modificar los elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario:
    print(termino)

for termino, valor in diccionario.items():
    print(termino, valor)

#Otras de acceder a un diccionario
for termino in diccionario.keys():#Muestra solo las llaves
    print(termino)

for valor in diccionario.values():# Muestra solo los valores de las llaves
    print(valor)

#Comprobar la existencia de algun elemento
print('IDE' in diccionario)

#Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

#Eliminar un elemento
diccionario.pop('SARD')
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

#Eliminar diccionario
#del diccionario
#print(diccionario)

# Concatenamos Listas
Lista1 = [1, 2, 3, 1]
Lista2 = [4, 5, 6, 1]
Lista3 = Lista1 + Lista2
print(Lista3)

Lista3.extend([7, 8, 9, 1])# Se utililza para agregar varios elementos a una lista
print(Lista3)

print(Lista3.index(5)) # Función para ubicar en que indice esta el valor ingresado

#Como saber cuantos valores repetidos hay dentro de una lista
print(Lista3.count(1)) #Cuenta cuantos valores iguales hay dentro de una lista

#Para poner al revez un lista
Lista3.reverse()
print(Lista3)

#Para que una lista se multiplique repitiendo sus elementos
Lista3 = Lista3 * 2
print(Lista3)

#Metodos de ordenamiento
Lista3.sort()
print(Lista3)

Lista3.sort(reverse=True) #Ordenamiento Descendente
print(Lista3)

#Repaso de Tuplas
tupla = (4, "Hola", 6.78, [1, 2, 78], 4, 'Hola')
print(tupla)

print(4 not in tupla)# Accion booleana, su respuesta es de tipo booleana
# lo que podes usar dentro de tuplas son: index, count, len
# En tuplas se puede convertir de tupla a lista de lista a tupla

#Repaso de set o conjunto
#Definir un conjunto
conjunto2 = set()
conjunto1 = {'Bye', }
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('Hola')
print(conjunto1)
print(3 not in conjunto1)

#Como hacer la igualdad de 2 conjuntos
print(conjunto1 == conjunto2) #Booleano


#Operaciones en conjuntos

conjunto3 = conjunto1 | conjunto2 #La linea une los conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 #que elemento tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 #que elemento esta en el conjunto1 y no en el 2
print(conjunto3)

conjunto3 = conjunto2 - conjunto1 #que elemento esta en el conjunto2 y no en el 1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 #Elementos que no comparten o que son diferentes
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3))#Aqui preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))

print(conjunto3.issuperset(conjunto1))#Preguntamos si los elementos del conjunto1 entan dentro del 3
print(conjunto3.issuperset(conjunto2))
print(conjunto2.issuperset(conjunto3))
 # Como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en común
print(conjunto1.isdisjoint(conjunto2)) # No hay cosas en común

#Convertir un conjunto totalmente inmutable
conjunto1 = frozenset #esto hace que el conjunto sea totalmente inmutable
# No se puede agregar, modificar ni eliminar elementos del conjunto

# Repaso Diccionarios
diccionarioNuevo = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)
#Como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferente tipos de datos
diccionario2 = {'Ariel': {"Edad":40, "Altura": 1.83}, "Olvaldo": [45, 1.85], 'Natalia': [35, 1.67]}
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre': "Lionel Messi", "Edad": 35, "Altura": 1.70, "Precio": "50 Millones", "Posicion": 'Extremo Derecho'},
    11: {'Nombre': "Angel Di Maria", "Edad": 34, "Altura": 1.80, "Precio": "15 Millones", "Posicion": 'Extremo Derecho'},
    21: {'Nombre': "Paulo Dybala", "Edad": 28, "Altura": 1.77, "Precio": "35 Millones", "Posicion": 'MediaPunta'},
    24: {'Nombre': "Enzo Fernandez", "Edad": 23, "Altura": 1.70, "Precio": "110 Millones", "Posicion": 'MedioCampista'},
    19: {'Nombre': "Julian Alvarez", "Edad": 23, "Altura": 1.80, "Precio": "90 Millones", "Posicion": 'Delantero Centro'},
    23: {'Nombre': "Emiliano Martinez", "Edad": 30, "Altura": 1.98, "Precio": "60 Millones", "Posicion": 'Arquero'},
    17: {'Nombre': "Cuti Romero", "Edad": 25, "Altura": 1.97, "Precio": "200 Millones", "Posicion": 'Defensor Central'},
    9: {'Nombre': "Lautaro Martinez", "Edad": 26, "Altura": 1.82, "Precio": "120 Millones", "Posicion": 'Delantero Centro'},
    16: {'Nombre': "Lisandro Martinez", "Edad": 25, "Altura": 1.75, "Precio": "70 Millones", "Posicion": 'Defensor Central'}
}
for llave, valor in seleccionArgentina.items():
    print(llave, valor)
print("Tenemos cargados en el diccionario la cantidad de Jugadores: ", end='')
print(len(seleccionArgentina))

#Oulas usando listas
pila = [1, 2, 3]
#Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

#Sacamos elementos por el final
elementoBorrado = pila.pop()
print(f'Sacamos el elemento {elementoBorrado}')
print(f'la pila ahora quedo asi: {pila}')

#Colas con listas
#Estructura de datos tipo fifo (First input / first output)
cola = ["ariel", "Osvaldo", "Liliana", "Pilar"]
cola.append("Natalia")
cola.append("Jose")
print(cola)
#Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'antendido el cliente: {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'antendido el cliente: {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'antendido el cliente: {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'antendido el cliente: {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'antendido el cliente: {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'antendido el cliente: {seRetira}')
print(cola)