total_medicamentos = 100
total_pacientes = 20

# 1. Operaciones
dosis_por_paciente = total_medicamentos / total_pacientes
print("repartir_dosis")
print(dosis_por_paciente)

# 2. Validaciones lógicas
medicamentos_entregados = total_medicamentos > total_pacientes
print(medicamentos_entregados)

alerta_escasez = not medicamentos_entregados
print(alerta_escasez)

# 3. Pruebas
print(total_medicamentos == total_pacientes)

resultado = total_medicamentos != total_pacientes
print(resultado)

print(total_medicamentos == total_pacientes)
print(total_medicamentos != total_pacientes)