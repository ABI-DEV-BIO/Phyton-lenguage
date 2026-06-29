#1. DATA
recursos_disponibles=100
recursos_consumidos=60
meta_de_ahorro=50

#2. RECURSOS
recursos_restantes=recursos_disponibles-recursos_consumidos
print(recursos_restantes)

#3. META
cumple_meta=recursos_restantes>=recursos_consumidos
print(cumple_meta)