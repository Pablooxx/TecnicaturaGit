#Ejercicio 3: Agregar personajes a una lista
# Escribir un programa donde cree una lista con los siguientes personajes del señor de los anillos
#Nombre: Aragon
#Clase: Guerrero
#Raza: Dúnadan del norte
#Nombre: Gandalf
#Clase: Mago
#Raza: Istar
#Nombre: Legolas
#Clase: Arquero
#Raza: Elfo Sindar

personajes = [] #Creamos una lista vacia
#Creamos diccionarios
P = {"Nombre": "Aragon", "Clase": "Guerrero", "Raza": "Dúnadan del Norte"}
personajes.append(P) #Agregamos a la lista un personaje
P = {"Nombre": "Gandalg", "Clase": "Mago", "Raza": "Istar"}
personajes.append(P)
P = {"Nombre": "Legolas", "Clase": "Arquero", "Raza": "Elfo Sindar"}
personajes.append(P)
print(personajes)