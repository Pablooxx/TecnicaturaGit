class MiClase:
    variable_clase = 'Esta es una variable de clase'
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

print(MiClase.variable_clase)
miclase1 = MiClase('Esta es una variable de instancia')
print(miclase1.variable_instancia)
print(miclase1.variable_clase)
miClase2 = MiClase('Esta es otra prueba de variable de instancia')
print(miClase2.variable_clase)
print(miClase2.variable_instancia)