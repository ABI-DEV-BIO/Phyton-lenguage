#1.Data
total_virus=50
areas_vulnerables=4
antivirus=60

#.2.Distribution
antivirus_por_zona=total_virus+areas_vulnerables+antivirus
print("Repartir_antivirus")
print(antivirus_por_zona)

#3.Sistem
sistema_protegido=antivirus>total_virus
print(sistema_protegido)

#4.Sistem
alerta_peligro = not sistema_protegido
print(alerta_peligro)