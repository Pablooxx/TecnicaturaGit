# Ejercicio Etapas de la Vida según la edad

edad = int(input('Digite su edad: '))
mensaje = None
if 0 <= edad < 10:
    mensaje = 'La infancia es increible y bella'
elif 10 <= edad < 20:
    mensaje = 'Tiene muchos cambios, mucho que estudiar'
elif 20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo'
elif 30 <= edad < 40:
    mensaje = 'Comienza la nueva vida y nuevos aprendizajes'
elif 40 <= edad < 50:
    mensaje = 'La vida es prospera y enseñas a vivirla'
elif 50 <= edad < 60:
    mensaje = 'Acompañas y te acompañan en el viaje'
elif 60 <= edad < 70:
    mensaje = 'El ocaso'
elif 70 <= edad < 80:
    mensaje = 'Los últimos momentos'
elif 80 <= edad < 90:
    mensaje = 'deja de robar'
elif 90 <= edad < 100:
    mensaje = 'Abeja Rebelde le dicen a este...'
else:
    mensaje = 'Error, etapada de vida no reconocida'
print(f'Tu edad es: {edad}, {mensaje}')