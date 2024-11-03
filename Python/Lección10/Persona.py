class Persona:
    contador_personas = 0 # variable de clase

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1 #vamos incrementando
        return cls.contador_personas
    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona[{self.id_persona} = {self.nombre} {self.edad}]'

persona1 = Persona('Pablo', 28)
print(persona1)
persona2 = Persona('Ariel', 28)
print(persona2)
persona3 = Persona('liliana', 40)
print(persona3)
Persona.generar_siguiente_valor()
persona4 = Persona('javier', 32)
print(persona4)
print(f'Valor contador personas: {Persona.contador_personas}')