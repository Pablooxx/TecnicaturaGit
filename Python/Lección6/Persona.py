class Persona:  #Creamos una clase
    def __init__(self, nombre, apellido, edad): # Se lo llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

persona1 = Persona('Ariel', 'Betancud', '40')#Necesitamos enviar argumentos
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} su edad es: {persona1.edad}')

persona2 = Persona('Pablo', 'Aparicio', '28')
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} su edad es: {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Perez'
persona1.edad = 38
print(f'El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} su edad es: {persona1.edad}')

# Los atributos son: caracteristicas
# Los métodos son: el comportamiento que van a tener los objetos (Acciones)

persona1.mostrar_detalle()
persona2.mostrar_detalle()
