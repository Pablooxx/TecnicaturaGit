class Persona:  #Creamos una clase
    def __init__(self, nombre, apellido,dni, edad, *args, **kwargs): # Se lo llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni# Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
    def mostrar_detalle(self): #seld es igual a this
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la dirección es: {self.args}, los datos importantes son: {self.kwargs}')

persona1 = Persona('Ariel', 'Betancud',5465, 40)#Necesitamos enviar argumentos
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} su edad es: {persona1.edad}')

persona2 = Persona('Pablo', 'Aparicio',4565, '28')
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} su edad es: {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Perez'
persona1.edad = 38
print(f'El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} su edad es: {persona1.edad}')

# Los atributos son: caracteristicas
# Los métodos son: el comportamiento que van a tener los objetos (Acciones)

persona1.mostrar_detalle()#la referencia en este caso se pasa de manera automatica
persona2.mostrar_detalle()

#Persona.mostrar_detalle(persona1) #Debemos pasarle una referencia para el self o dara error
persona1.telefono = '123456'
print(f'Este es el telefono de {persona1.nombre}: {persona1.telefono}') # Hemos creado un atributo de un objeto

# print(persona2.telefono) el objeto persona2 no tiene este atributo, da error
persona3 = Persona('Rogelio', 'Romero',4565, 22, 'Telefono', '4654654', 'Calle Lopes', 823, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=105, CFavorito= 'Rojo', Auto= 'Citröen', Modelo=2021 )
persona4 = Persona('Pablo', 'Aparicio', 5465,28, 'Telefono', '3816454648', 'Balcarce', 573, 'Piso', 15, 'Dpto', 1, Altura=1.86, Peso=103, CFavorito= 'Azul', Auto= 'Peugeot', Modelo=2019 )

persona3.mostrar_detalle()
persona4.mostrar_detalle()
#print(persona3._dni) Esto no se debe utilizar esta encapsulado, esto dice que lo desconocemos Python
#persona3.__nombre # Esta totalmente Capsulado


