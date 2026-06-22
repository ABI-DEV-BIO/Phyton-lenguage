#1.Usuarios y regalos
usuarios_activos=5000
regalos_de_temporada=4000

#2.Repartir regalos
regalos_por_persona = regalos_de_temporada / usuarios_activos

print("repartir regalos")
print(regalos_por_persona)

#3.Verificar 1 y 2
suficientes_regalos = regalos_de_temporada > usuarios_activos
print(suficientes_regalos)

#4.Verificar escazes
alerta_sistema=not suficientes_regalos
print(alerta_sistema)

#5.Verificar igualdad
print(usuarios_activos==regalos_de_temporada)
print(usuarios_activos!=regalos_de_temporada)