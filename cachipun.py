# ----- JUEGO PIEDRA PAPEL Y TIJERA--------

# AUTHOR : MARELY

# REGLAS DEL JUEGO

# Jugadores: El juego se juega entre dos personas1.

# Movimientos: Los jugadores cuentan juntos hasta tres y simultáneamente eligen una de las siguientes array_gameOptiones
# : piedra, papel o tijera12.

# Determinar al ganador: Las reglas para determinar al ganador son las siguientes12:

#Piedra gana a tijera: La piedra rompe la tijera.
#Tijera gana a papel: Las tijeras cortan el papel.
#Papel gana a piedra: El papel envuelve la piedra.
#Si los dos jugadores hacen el mismo signo, no se suma ningún punto y se repite el turno12.
#Fin del juego: El juego puede durar lo que los jugadores quieran, por ejemplo, gana el jugador que llega primero a sumar 10 puntos3.

import random

# Constantes para las array_gameOptiones del juego
PIEDRA = 1
PAPEL = 2
TIJERA = 3
SALIR = 0

# Lista de array_gameOptiones, opciones del juego
array_gameOptiones  = ["", "piedra", "papel", "tijera"]


#Función obtener_opcion_usuario.
def obtener_opcion_usuario():
    while True:
        try:
            opcion = int(input("Ingrese el número correspondiente para jugar: "))
            if opcion in [PIEDRA, PAPEL, TIJERA, SALIR]:
                return opcion
            else:
                print("Número inválido. Por favor, intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

def obtener_opcion_computador():
    return random.choice([PIEDRA, PAPEL, TIJERA])



#Funcion determinar_ganador. Esta función determina quien es el ganador en función de los parametros recibidos (usuario,)
def determinar_ganador(usuario, computador):
    if usuario == computador:
        return "Es un empate!😏"
    elif (usuario == PIEDRA and computador == TIJERA) or \
        (usuario == PAPEL and computador == PIEDRA) or \
        (usuario == TIJERA and computador == PAPEL):
        return "¡Ganaste! 😊🙌"
    else:
        return "Perdiste 😢 ¡Inténtalo de nuevo!"



#Función jugar. Aquí se inicia la partida desplegando el juego en pantalla.
def jugar():
    print("\n#############################################")
    print("             Piedra, papel o tijera")
    print(f"              [{PIEDRA}] piedra")
    print(f"              [{PAPEL}] papel")
    print(f"              [{TIJERA}] tijera")
    print(f"              [{SALIR}] salir")
    print("#############################################")

    while True:
        opcion_usuario = obtener_opcion_usuario()
        if opcion_usuario == SALIR:
            break

        opcion_computador = obtener_opcion_computador()

        print(f"\nHas elegido: {array_gameOptiones
		[opcion_usuario]}")
        print(f"Computador eligió: {array_gameOptiones
		[opcion_computador]}")

        resultado = determinar_ganador(opcion_usuario, opcion_computador)
        print(f"\n{resultado}")

        continuar = input("\n¿Quieres seguir jugando? (s/n): ")
        if continuar.lower() != 's':
            break

# Ejecutar el juego
jugar()

