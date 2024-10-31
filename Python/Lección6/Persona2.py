class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property # decorador
    def nombre(self):#metodo Getter
        print('Estamos utilizando el método get: ')
        return self._nombre
    @nombre.setter
    def nombre(self, nombre): #Metodo Setter
        print('Estamos utilizando el método Set: ')
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__':
    persona1 = Persona2('Ariel', 'Betancud', 41)
    print(persona1.nombre)
    print(persona1.apellido)
    print(persona1.edad)#Llamamos al método getter
    persona1.nombre = ('Juan Pedro')#Llamamamos al metodo setter
    print(persona1.nombre)
    print(persona1.mostrar_detalle())

    # Tarea crear tres onjetos más utilizando losmétodos getter and setter
    # para modificar y mostrar los cambios

    persona2 = Persona2('Flor', 'Romero', 23)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = 'Florencia'
    persona2.apellido = 'Romery'
    persona2.edad = 22
    print(persona2.mostrar_detalle())

    persona3 = Persona2( 'Caro', 'Felisa', 21)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.nombre = 'Carolina'
    persona3.apellido = 'Feliz'
    persona3.edad = 31

    print(persona3.mostrar_detalle())

    persona4 = Persona2('Pablo', 'Aparicio', 23)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = 'Pabloncho'
    persona4.apellido = 'Apari'
    persona4.edad = '28'
    print(persona4.mostrar_detalle())

print(__name__)