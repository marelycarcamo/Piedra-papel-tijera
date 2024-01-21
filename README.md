# Juego Piedra, Papel, Tijera

<p align="justify">Este es un juego interactivo de <b>Piedra, Papel, Tijera </b> implementado en Python. Es una excelente demostración de las habilidades de programación y resolución de problemas.</p>

## Descripción

1. <p align="justify"><b> Inicio del juego. </b> Cuando se inicia el juego, se muestra un menú con las opciones disponibles: piedra, papel, tijera y salir. El usuario debe seleccionar una opción ingresando el número correspondiente. </p>

2. <p align="justify"><b> Elección del jugador.</b> El jugador elige su movimiento ingresando el número correspondiente a piedra (1), papel (2), tijera (3) o salir (0). Si el jugador ingresa un número no válido, se le pide que intente de nuevo.</p>

3. <p align="justify"><b> Elección de la computadora.</b> La computadora elige su movimiento de manera aleatoria utilizando la función random.choice. Esta función selecciona un elemento al azar de la lista de opciones (piedra, papel, tijera).</p>

4. <b> Determinación del ganador.</b> Se determina el ganador de la ronda comparando el movimiento del jugador con el de la computador:
   - Piedra gana a tijera (la piedra rompe la tijera).
   - Tijera gana a papel (las tijeras cortan el papel).
   - Papel gana a piedra (el papel envuelve la piedra).
   - Si ambos jugadores eligen el mismo movimiento, es un empate.

5. <p align="justify"><b>  Fin de la ronda.</b> Después de determinar el ganador, se muestra el resultado de la ronda al jugador. Si el jugador ganó, se muestra un mensaje de felicitación. Si la computadora ganó, se muestra un mensaje de aliento para que el jugador lo intente de nuevo. Si fue un empate, se informa al jugador del empate.</p>

6. <p align="justify"><b> Continuación del juego.</b> Después de cada ronda, se le pregunta al jugador si desea seguir jugando. Si el jugador elige seguir jugando, se inicia una nueva ronda. Si el jugador elige salir, el juego termina.</p>
