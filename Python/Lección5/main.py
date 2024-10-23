#Comenzamos con funciones

#Definimos una función
def mi_funcion():
    print('Saludos a todos los alumnos de la tecnicatura')

mi_funcion() #estamos llamando a la función
mi_funcion()# Se puede llamar a una funcion N cantidad de veces
mi_funcion()

# Desempaquetado de listas o list unpacking
def show (name, lastname):
    print(name+' '+lastname)
person = ["Pablo", "Aparicio"]
show(person[0], person[1])#Pasamos uno por uno los datos de la lista a la función
show(*person)#esto es lo mismo pero le pasamos todo junto
person2 = ('Gaston', 'Fuenzalida')
show(*person2)
person3 = {"lastname": "Lucero", "name": "Natalia"}
show(**person3)

numbers =[1, 2, 3, 4, 5]
for n in numbers:
    print(n)
else:
    print('Esto se termino')

# List comprehension, lista de comprensión
names = ["Pablo", "Rodrigo", "Luz", "Gaston"]
alongP = [p for p in names if p[0] == 'P']#Esto regresa una nueva lista
print(alongP)

bottleC = [{"name": 'Quilmes', 'country': 'Arg'},
           {'name': 'Corona', 'country': 'Mx'},
           {'name': 'Stella Artois', 'country': 'Belgium'},
           ]
Arg = [b for b in bottleC if b['country'] == 'Arg']
print(Arg)
print(bottleC)

#Paso de argumentos (funciones)
def mi_funcion2(name, lastname):
    print('Saludos a todos lo que ven a traces del canal de YouTube')
    print(f'Nombre: {name}, Apellido: {lastname}')
mi_funcion2('Jorge', 'Lucero')
mi_funcion2('pablo', 'aparicio')

#La palabra return en funciones
#creamos una función para sumar
def sumar(a, b):
    return a + b
#resultado = sumar(78, 22)
#print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es {sumar(55,45)}')

def sumar2(a:int = 0, b:int = 0):# le damos un valor por default
    return a + b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22, 66)}')

# Argumentos, variables en funciones
def listarnombres(*nombres):#normanmente se utiliza: *args
    for nombre in nombres:#se va a convertir en tuplas que no se modifica
        print(nombre)
listarnombres("lucas", 'pablo', 'Claudia', 'Rosa')
listarnombres("lucasante", 'pablox', 'Cla', 'Ricardo')

def listarTerminos(**terminos): # lo mas utilizado es **kwargs para recibir argumentos
    for llave, valor in terminos.items():#kwarg: key word argument
        print(f'{llave} : {valor}')

listarTerminos()#no recibe nada
listarTerminos(IDE='Integrated Development Enviroment', PK='Primary KEY')
listarTerminos(nombre='Leonel Messi')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('carla')
#desplegarNombres(10) No es un objeto iterable
desplegarNombres((10, 11))#La convertimos en una tupla
desplegarNombres([22, 55])#La convertimos en una lista

#Funciones Recursivas
def factorial(numero):
    if numero == 1:#case base
        return 1
    else:
        return numero * factorial(numero-1) #Caso Recursivo

resultado = factorial(int(input('Ingrese un número para calcular el factorial: ')))
print(f'El factorial del número es: {resultado}')