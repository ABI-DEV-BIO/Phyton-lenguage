def mostrar_tabla():
    print("------------------------------------------")
    print("VUELOS DISPONIBLES A LONDRES:")
    print("1. Aeroméxico - Salida: 10:00 AM - $15,000")
    print("2. British Airways - Salida: 02:00 PM - $18,000")
    print("3. Iberia - Salida: 08:00 PM - $14,500")
    print("------------------------------------------")

print("BOBBY 3.0")
nombre = input("¿Quién eres?: ")

if nombre.lower() == "abi":
    print("¡Acceso concedido!")
    print("BOT: Ey, ¿qué tal, cómo estás amigo?")
    
    
    estado = input()
    
    if estado.lower() == "bien":
        print("BOBBY: ¡Super bro, me alegro por ti!")
        print("BOBBY: ¿Y qué tienes en mente?")
        
        
        accion = input()
        if accion.lower() == "viajar":
            print("BOBBY: ¡Wow bro, es una excelente idea!")
            print("BOBBY: Dime a dónde quieres ir y te mando los vuelos disponibles")
            
            destino = input()
            if destino.lower() == "londres":
                print("Ey bro, todo listo, aquí tienes los datos:")
                mostrar_tabla()
            else:
                print("BOBBY: Oh entiendo, no te preocupes, será para la otra.")
        else:
            print("BOBBY: Entiendo, aquí estaré.")
    else:
        print("BOBBY: Lo siento hermano, puedo ayudarte en algo?")
else:
    print("SISTEMA: LO SIENTO, NO RECONOZCO ESE USUARIO")
