class Persona():
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self,edad):
        self._edad = edad

    def __str__(self):#Override = Sobreescribir
        return f'Persona: Nombre: {self._nombre} Edad: {self.edad}'
class Empleado(Persona):
    def __init__(self, _nombre, _edad, sueldo):#Esta clase es hija de la clase persona
        super().__init__(_nombre, _edad)
        self._sueldo = sueldo
    @property
    def sueldo(self):
        return self._sueldo
    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado: [Sueldo: {self._sueldo}] {super().__str__()}'

empleado1 = Empleado('Pablo', 28, 75000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)

#Tarea: encapsular los atrinutos y agregar los métodos getters and setters
# Crear otro objeto, pasar los datos para nobre, edad y sueldo
# Mostrar estos datos, luego modificar y mostrar nuevamente

empleado2 = Empleado('Liliana', 38,70000)
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)
empleado2.nombre = 'Natalia'
empleado2.edad = 34
empleado2.sueldo = 80000
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)

