# Futbolistas

import random, time
"""
Compromiso:
    Crear la clase
    _____________________
    |* Futbolista       |
    |-------------------|
    |- nombre           |
    |- goles            |
    |- lesiones         |
    |- tamarillas       |
    |- trojas           |
    |-------------------|
    |- patear()         |
    |- fautear()        |
    |- hacer_gol()      |
    |- hacer_lesion()   |
    |-------------------|

Crear minimo 4 futbolistas
Costruir una dinamica que genere goles, lesiones, saquen tarjetas rojas y amarillas.
Finaliza  por cantidad  de lesiones  de un jugador o por tiempo (libreria time)
"""

# Definimos la clase Futbolista
class Futbolista:
    # Inicializador de la clase Futbolista
    def __init__(self, nombre,):
        self.nombre = nombre  # Nombre del futbolista
        self.goles = random.randint(0, 1)  # Se asigna aleatoriamente entre 0 o 1 goles al jugador al inicio
        self.lesiones = 0  # Contador de lesiones inicializado en 0
        self.tamarillas = 0  # Contador de tarjetas amarillas inicializado en 0
        self.trojas = 0  # Contador de tarjetas rojas inicializado en 0
        self.expulsado = False  # Estado del jugador, no expulsado al inicio
        
    # Método para mostrar las estadísticas del jugador
    def fichas(self):
        print(f"\n\t ⚽ {self.nombre} ⚽ ")
        print(f" - 🥅 Goles:\t\t{self.goles}")  # Muestra la cantidad de goles
        print(f" - 🩺 Lesiones:\t\t{self.lesiones}")  # Muestra la cantidad de lesiones
        print(f" - 🟨 Tamarillas:\t{self.tamarillas}")  # Muestra la cantidad de tarjetas amarillas
        print(f" - 🟥 Trojas:\t\t{self.trojas}")  # Muestra la cantidad de tarjetas rojas
        
    # Método para simular que el jugador patea el balón
    def patear(self):
        print(f"El jugador {self.nombre} ha pateado el balon")
        
    # Método que simula una falta cometida por el jugador
    def faulear(self):
        if not self.expulsado:  # Solo se cuenta la falta si el jugador no está expulsado
            self.tamarillas += 1  # Incrementa la cantidad de tarjetas amarillas
            print(f"El jugador {self.nombre} ha cometido una falta. Total amarillas: {self.tamarillas}")
            if self.tamarillas == 2:  # Si el jugador recibe 2 amarillas, se expulsa
                print(f"{self.nombre} ha recibido 2 tarjetas amarillas y es expulsado con una tarjeta roja.")
                self.recibir_roja()  # Llama al método que maneja la tarjeta roja
            
    # Método que asigna tarjeta roja y expulsa al jugador
    def recibir_roja(self):
        self.trojas += 1  # Incrementa la cantidad de tarjetas rojas
        self.expulsado = True  # Cambia el estado del jugador a expulsado
        print(f"{self.nombre} ha sido expulsado con una tarjeta roja. Total rojas: {self.trojas}")

    # Método para simular que el jugador hace un gol
    def hacer_gol(self):
        if not self.expulsado:  # El jugador solo puede hacer goles si no está expulsado
            self.goles += 1  # Incrementa la cantidad de goles
            print(f"¡Gooool de {self.nombre}! Total de goles: {self.goles}")
    
    # Método que incrementa el contador de lesiones del jugador
    def hacer_lesion(self):
        self.lesiones += 1  # Incrementa la cantidad de lesiones
        print(f"{self.nombre} ha sido lesionado. Total de lesiones {self.lesiones}")

# Función para simular un partido entre futbolistas con una duración específica
def partido(futbolistas, duracion_partido):
    inicio_partido = time.time()  # Marca el tiempo de inicio del partido
    
    # El bucle continúa hasta que el tiempo transcurrido supera la duración del partido
    while time.time() - inicio_partido < duracion_partido:
        # Selecciona los jugadores que aún no han sido expulsados
        jugadores_disponibles = [jugador for jugador in futbolistas if not jugador.expulsado]
        if not jugadores_disponibles:  # Si todos los jugadores han sido expulsados, el partido termina
            print("Todos los jugadores han sido expulsados. El partido ha terminado.")
            break

        jugador = random.choice(jugadores_disponibles)  # Selecciona un jugador aleatorio de los disponibles
        
        # Genera un evento aleatorio: gol, lesión o falta
        evento = random.choice(["gol", "lesion", "faul"])
        
        # Ejecuta el evento seleccionado
        if evento == "gol":
            jugador.hacer_gol()  # Llama al método para hacer gol
        elif evento == "lesion":
            jugador.hacer_lesion()  # Llama al método para recibir una lesión
        elif evento == "faul":
            jugador.faulear()  # Llama al método para cometer una falta

        # Verifica si un jugador tiene demasiadas lesiones (3 o más)
        if jugador.lesiones >= 3:
            print(f"{jugador.nombre} ha sido lesionado demasiadas veces y ya no puede seguir jugando.")
            jugador.expulsado = True  # Expulsa al jugador del partido si tiene demasiadas lesiones

        # Pausa el bucle durante 1 segundo entre cada evento para simular tiempo real
        time.sleep(1)

    print("El tiempo ha terminado. El partido ha finalizado.")  # Mensaje cuando el partido termina por tiempo

# Crear instancias de jugadores
jugador_1 = Futbolista("Ronaldinho")
jugador_2 = Futbolista("René Higuita")
jugador_3 = Futbolista("Carlos Valderrama")
jugador_4 = Futbolista("Diego Maradona")

# Lista de jugadores
futbolistas = [jugador_1, jugador_2, jugador_3, jugador_4]

# Definir la duración del partido en segundos (por ejemplo, 20 segundos)
duracion_partido = 20

# Simula el partido
partido(futbolistas, duracion_partido)

# Muestra las estadísticas de cada jugador después del partido
jugador_1.fichas()
jugador_2.fichas()
jugador_3.fichas()
jugador_4.fichas()