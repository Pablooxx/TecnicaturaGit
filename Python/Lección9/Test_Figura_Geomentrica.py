from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

print('Creación de objeto clase Cuadrado'.center(50, '_'))
cuadrado1 = Cuadrado (8, 'Rojo')
cuadrado1.alto = 6
#print(cuadrado1.alto)
#print(cuadrado1.alto)
print(f'cálculo del área del cuadrado: {cuadrado1.calcular_area()}')


# MRO = Method Re--solution Order
#print(Cuadrado.mro())

print(cuadrado1)
print('Creación de objeto clase Rectangulo'.center(50, '_'))
rectangulo1 = Rectangulo(9, 3, 'verde')
rectangulo1.alto = 8
print(f'Calculo del area del rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

#figura1 = FiguraGeometrica()No se puede instancias, es abstracta
print(Cuadrado.mro())

