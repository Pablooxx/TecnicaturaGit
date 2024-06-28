def calcular_salarios(horas_trabajadas, tarifa_pago):
    salarios = []
    sumatoria_salarios = 0

    for horas in horas_trabajadas:
        salario = horas * tarifa_pago
        salarios.append(salario)
        sumatoria_salarios += salario

    return salarios, sumatoria_salarios

# solicitamos al usuario que ingrese las horas trabajadas y la tarifa de pago
horas_trabajadas = []
for i in range(5):
    horas = float(input(f"ingresa las horas trabajadas por la persona {i + 1}: "))
    horas_trabajadas.append(horas)

tarifa_pago = float(input("ingresa la tarifa de pago por hora: "))

# calculamos los salarios y la sumatoria de todos los salarios
salarios, sumatoria_salarios = calcular_salarios(horas_trabajadas, tarifa_pago)

# mostramos los resultados
for i in range(5):
    print(f"el salario de la persona {i + 1} es: {salarios[i]}")
print(f"la sumatoria de todos los salarios es: {sumatoria_salarios}")