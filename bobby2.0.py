print("BOBBY 1.0")
nombre = input("¿Quién eres?: ")

if nombre.lower() == "abinadab":
    print("¡Acceso concedido!")
    print("BOT: Ey que tal como estas amigo?.")
else:
    print("SISTEMA:LO SIENTO NO RECONOZCO ESE USUARIO")

user_input=input()

print("BOBBY: !Super bro me alegro por ti")
print(f"BOBBY:Y que me cuentas bro?")

user_input=input()

print("BOBBY:!Wow bro es una excelente idea!")
print("BOBBY:!Y dime a que parte del mundo te gustaria hacerlo?")

user_input=input()

print(f"BOBBY:¡Genial bro quieres que investigue vuelos disponibles en tu zona?")

user_input=input()

print("Claro hermano aqui tienes los horarios y las aerolineas disponibles")
def mostrar_tabla():
    print("---------------------------------------------------------")
    print("AEROLINEA  VUELO    ORIGEN      DESTINO     HORARIO")
    print("---------------------------------------------------------")
    print("Global Sky GS 402   Mexico      Londres     08:30 20:45")
    print("EuroJet    EJ 119   Nueva York  Londres     12:15 23:30")
    print("Oceanic    OC 77    Zurich      Londres     10:00 11:20")
    print("SkyLink    SL 505   Madrid      Londres     15:45 17:00")
    print("---------------------------------------------------------")

print("Ey bro todo listo aquí tienes los datos:")
mostrar_tabla()