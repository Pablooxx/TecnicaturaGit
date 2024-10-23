# Ejercicio 5: convertidor de temperaturas
# REalizar dos funciones para convertir de grados celsius
# a fahrenheit y viseversa.
# Investigar las formulas

# Función que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32 # la presedencia: *,/,+
#Función que convierte de fahrenheit a celsius
def fharenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 # la presedencia -,*,/

celsius = float(input('Digite el valor de Celsius: '))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} C a F -> {resultado:.2f}')

fahrenheit = float(input('Digite el valor de Fahrenheit: '))
resultado = fharenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C -> {resultado:.2f}')