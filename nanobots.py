#Titulo:
print("REPARTIR NANOBOTS")

#2.Dates
bio_robots=100
celulas_dañadas=40

#3.Distribute
nanobots_por_celula=bio_robots/celulas_dañadas
print(nanobots_por_celula)

#4.Suficientes?
unidades_usables=bio_robots<celulas_dañadas
print(unidades_usables)

#5.Alerta activada?
alerta_sistema=not bio_robots
print(alerta_sistema)

#6.Igualdad
print(bio_robots!=celulas_dañadas)
print(bio_robots==celulas_dañadas)

# Message
nanobots_dañados = 7
celulas_curadas = 9
print(f"{nanobots_dañados} nanobots dañados and {celulas_curadas} celulas curadas")

celulas=40
print(f"quedan {celulas} celulas")