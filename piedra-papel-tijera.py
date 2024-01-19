# ----- JUEGO PIEDRA PAPEL Y TIJERA--------

# REGLAS DEL JUEGO

# Jugadores: El juego se juega entre dos personas1.

# Movimientos: Los jugadores cuentan juntos hasta tres y simultáneamente eligen una de las siguientes opciones: piedra, papel o tijera12.

# Determinar al ganador: Las reglas para determinar al ganador son las siguientes12:

#Piedra gana a tijera: La piedra rompe la tijera.
#Tijera gana a papel: Las tijeras cortan el papel.
#Papel gana a piedra: El papel envuelve la piedra.
#Si los dos jugadores hacen el mismo signo, no se suma ningún punto y se repite el turno12.
#Fin del juego: El juego puede durar lo que los jugadores quieran, por ejemplo, gana el jugador que llega primero a sumar 10 puntos3.


import random

# Definición de las opciones del juego
opciones = ["piedra", "papel", "tijera"]

while True:
    print("\n#############################################")
    print("             Piedra, papel o tijera")
    print("              [1] piedra")
    print("              [2] papel")
    print("              [3] tijera")
    print("              [0] salir")
    print("#############################################")
    print("Ingrese el número correspondiente para jugar")

    # Obtener la elección del jugador
    eleccion_jugador = input("jugar: ")

    # Verificar si el jugador quiere salir del juego
    if eleccion_jugador == "0":
        break

    # Verificar si la elección del jugador es válida
    while eleccion_jugador not in ["1", "2", "3"]:
        print("Número inválido. Por favor, intente de nuevo.")
        eleccion_jugador = input("Ingrese un número: ")

    # Convertir la elección del jugador a piedra, papel o tijera
    eleccion_jugador = opciones[int(eleccion_jugador) - 1]

    print(f"\nHas elegido: {eleccion_jugador}")

    # Elección aleatoria de la computadora
    eleccion_computadora = random.choice(opciones)

    print(f"Computadora eligió: {eleccion_computadora}")

    # Determinar el ganador
    if eleccion_jugador == eleccion_computadora:
        print("\nEs un empate!")
    elif (eleccion_jugador == "piedra" and eleccion_computadora == "tijera") or \
         (eleccion_jugador == "papel" and eleccion_computadora == "piedra") or \
         (eleccion_jugador == "tijera" and eleccion_computadora == "papel"):
        print("\n¡Ganaste!")
    else:
        print("\nPerdiste. ¡Inténtalo de nuevo!")

    # Preguntar al jugador si quiere continuar
    continuar = input("\n¿Quieres seguir jugando? (s/n): ")
    if continuar.lower() != 's':
        break
    