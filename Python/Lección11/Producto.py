class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1 #Aumento de variable
        self._id_producto = Producto.contador_productos #Llamador de la variable
        self._nombre = nombre
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, precio):
        self._precio = precio

    #Sobreescribimos el metodo str
    def __str__(self):
        return f'Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio} '

if __name__ == '__main__':
    prducto1 = Producto('Camiseta', 100.00)
    print(prducto1)
    prducto2 = Producto('Pantalon', 150.00)
    print(prducto2)