print("SISTEMA DE SEGURIDAD")

contraseña_ingresada=171224
contraseña_guardada=171224

print(contraseña_ingresada==contraseña_guardada)

if contraseña_guardada==contraseña_ingresada:
    print("¡Acceso concedido, bienvenido Abi 🔓") 

    #2 SENSOR
    estado_seguro="sin_movimiento"
    estado_sensor="movimiento_detectado"

    #3.
    alarma_activa=estado_seguro!=estado_sensor
    print("ALARMA")
    print(alarma_activa) 