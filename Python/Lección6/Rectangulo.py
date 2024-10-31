class Rectangulo:
    """
    Crear una clase llamada Rectangulo, debe rtener 2 atributos: altura y base
    el nombre del método será calcular area utilizando la formula:
    area = base * altura. Pero la base y la altura deben ser ingresadas
    por el usuario y los objetos deben ser tres.
    """
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
    def calcular_area(self):
        return self.altura * self.base

base = int(input('Digite el número para la base del rectangulo: '))
altura = int(input('Digite el número para la altura del rectangulo: '))
rectangulo1 = Rectangulo(base, altura)
if base == altura:
    print(f'esto es un cuadrado con area de: {rectangulo1.calcular_area()}')
else:
    print(f'El area del rectangulo es: {rectangulo1.calcular_area()}')