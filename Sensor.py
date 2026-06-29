print("SISTEMA DE SEGURIDAD")

contraseña_ingresada=171224
contraseña_guardada=171224

print("ACCESO")
print(contraseña_ingresada==contraseña_guardada)

#2 SENSOR
estado_seguro="sin_movimiento"
estado_sensor="movimiento_detectado"

#3.ALARMA
alarma_activa=estado_seguro!=estado_sensor
print("ALARMA")
print(alarma_activa)