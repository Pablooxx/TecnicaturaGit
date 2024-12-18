class Vehiculo:
    """
    Definir una clase padre llamada Vehiculo y dos clases hijas llamadas
    Auto y Bicicleta, las cuales heredan de la clase padre Vehiculo. La clase
    padre debe tener los siguientes atributos y métodos:
    Vehiculo (clase padre)
    -Atributos (Color, ruedas)
    Métodos(__ini__() y __str__())

    Auto(clase hija de Vehiculo)
    -Atributos(velocidad(k/hr))
    -Métodos(__init__() y __str__())

    Bicicleta(Clase hija de Vehiculo)
    -Atributos(tipo(urbana/montaña/etc.)
    -método(__init__() y __str__()

    Crear un objeto de cada clase
    """

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'Color: ' + self.color + ', Ruedas: ' + str(self.ruedas)


class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + ', Velocidad(km/hr): ' + str(self.velocidad)


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ', Tipo: ' + self.tipo


#Primer objeto de la clase padre Vehiculo
vehiculo = Vehiculo('Blanco', 4)
print(vehiculo)
#Segundo objeto ded la clase Hijo Auto
auto = Auto('Amarillo', 4, 120)
print(auto)
#Tercer Objeto de la clase Hijo Bicicleta
bici = Bicicleta('Rojo', 2, 'BMX')
print(bici)
