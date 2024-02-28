# ----- JUEGO PIEDRA PAPEL Y TIJERA--------

# AUTHOR : MARELY

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

# Constantes para las opciones del juego
PIEDRA = 1
PAPEL = 2
TIJERA = 3
SALIR = 0


#Funcion obtener_opcion_usuario. Obtiene la opción del usuario desde la entrada estándar.
def obtener_opcion_jugador():
    
    while True:
        try:
            opcion = int(input("Ingrese el número correspondiente para jugar: "))
            if opcion in [PIEDRA, PAPEL, TIJERA, SALIR]:
                return opcion
            else:
                print("Número inválido. Por favor, intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")


#Funcion obtener_opcion_computador. Obtiene una opción aleatoria para la computadora.
def obtener_opcion_computador():
    return random.choice([PIEDRA, PAPEL, TIJERA])


#Funcion determinar_ganador. Determina el ganador del juego
def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Es un empate!"
    elif (usuario == PIEDRA and computadora == TIJERA) or \
        (usuario == PAPEL and computadora == PIEDRA) or \
        (usuario == TIJERA and computadora == PAPEL):
        return "¡Ganaste!"
    else:
        return "Perdiste. ¡Inténtalo de nuevo!"


#Función jugar. Despliegue del juego en pantalla.
def jugar():
    """Ejecuta el juego de piedra, papel o tijera."""
    print("\n#############################################")
    print("             Piedra, papel o tijera")
    print(f"              [{PIEDRA}] piedra")
    print(f"              [{PAPEL}] papel")
    print(f"              [{TIJERA}] tijera")
    print(f"              [{SALIR}] salir")
    print("#############################################")

    while True:
        opcion_usuario = obtener_opcion_jugador()
        if opcion_usuario == SALIR:
            break

        opcion_computadora = obtener_opcion_computador()

        print(f"\nHas elegido: {opcion_usuario}")
        print(f"Computadora eligió: {opcion_computadora}")

        resultado = determinar_ganador(opcion_usuario, opcion_computadora)
        print(f"\n{resultado}")

        continuar = input("\n¿Quieres seguir jugando? (s/n): ")
        if continuar.lower() != 's':
            break


# Ejecutar el juego
jugar()
