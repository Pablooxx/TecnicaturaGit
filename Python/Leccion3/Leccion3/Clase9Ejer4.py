def main():
    # inicializa una lista para almacenar las calificaciones
    calificaciones = []

    # lee las calificaciones de los 10 alumnos
    for i in range(10):
        calificacion = float(input(f"ingrese la calificacion del alumno {i + 1}: "))
        calificaciones.append(calificacion)

    # calcula el promedio
    promedio = sum(calificaciones) / len(calificaciones)

    # encuentra la calificacion mas baja
    calificacion_minima = min(calificaciones)

    # muestra los resultados
    print(f"el promedio de las calificaciones es: {promedio}")
    print(f"la calificacion mas baja es: {calificacion_minima}")


if __name__ == "_main_":
    main()