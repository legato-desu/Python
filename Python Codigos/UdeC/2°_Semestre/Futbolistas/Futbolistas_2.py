import random, time

"""
A modificar:
    Goles iniciados en cero
    Lesiones, tarjetas amarillas y rojas en aleatorio
    Creación de jugadores pedidos al usuario "cantidad de jugadores"
    Print de faltas al fauleado
"""

# Definimos la clase Futbolista
class Futbolista:
    # Inicializador de la clase Futbolista    
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del futbolista
        self.goles = 0  # Inicializa el contador de goles en 0
        self.lesiones = random.randint(0, 2)  # Lesiones aleatorias al inicio (0, 1 o 2)
        self.tamarillas = random.randint(0, 1)  # Tarjetas amarillas aleatorias al inicio (0 o 1)
        self.trojas = 0  # Inicializa el contador de tarjetas rojas en 0
        self.expulsado = False  # Indica si el jugador ha sido expulsado
        self.retirado_por_heridas = False  # Indica si el jugador se ha retirado por lesiones

    # Método para mostrar las estadísticas del jugador
    def fichas(self):
        print(f"\n\t ⚽ {self.nombre} ⚽ ")
        print(f" - 🥅 Goles:\t\t{self.goles}")  # Muestra la cantidad de goles
        print(f" - 🩺 Lesiones:\t\t{self.lesiones}")  # Muestra la cantidad de lesiones
        print(f" - 🟨 Tamarillas:\t{self.tamarillas}")  # Muestra la cantidad de tarjetas amarillas
        print(f" - 🟥 Trojas:\t\t{self.trojas}")  # Muestra la cantidad de tarjetas rojas

        # Mensaje si el jugador se ha retirado por lesiones
        if self.retirado_por_heridas:
            print(f"\t{self.nombre} sale por lesiones.")

    # Método para simular que el jugador patea el balón
    def patear(self):
        print(f"{self.nombre} ha pateado el balón")

    # Método que simula una falta cometida por el jugador
    def faulear(self):
        if not self.expulsado and not self.retirado_por_heridas:
            self.tamarillas += 1  # Aumenta la tarjeta amarilla
            print(f"{self.nombre} ha fauleado 🟨")
            if self.tamarillas == 2:  # Si acumula 2 tarjetas amarillas
                print(f"{self.nombre} volvió a faulear 🟨🟨")
                self.recibir_roja()  # Llama a la función para recibir tarjeta roja

    def recibir_roja(self):
        self.trojas += 1  # Aumenta la tarjeta roja
        self.expulsado = True  # Marca al jugador como expulsado
        print(f"{self.nombre} 🟥 expulsado")

    def hacer_gol(self):
        if not self.expulsado and not self.retirado_por_heridas:
            self.goles += 1  # Aumenta el contador de goles
            print(f"🎉 ¡Gooool de {self.nombre}!")

    def hacer_lesion(self):
        if not self.retirado_por_heridas:
            self.lesiones += 1  # Aumenta el contador de lesiones
            print(f"{self.nombre} 🚑 lesión")
            if self.lesiones >= 3:  # Si el jugador tiene 3 o más lesiones
                print(f"{self.nombre} se retira por lesiones")  # Mensaje de retiro
                self.retirado_por_heridas = True  # Marca al jugador como retirado

def crear_jugadores():
    cantidad = int(input("¿Cuántos jugadores deseas crear? "))  # Pregunta la cantidad de jugadores
    futbolistas = []  # Lista para almacenar los futbolistas
    for i in range(cantidad):
        nombre = input(f"Nombre del {i + 1}° jugador: ")  # Solicita el nombre del jugador
        futbolistas.append(Futbolista(nombre.capitalize()))  # Crea una instancia de Futbolista y la agrega a la lista
    return futbolistas  # Retorna la lista de futbolistas

def verificar_unico_jugador(futbolistas):
    # Filtra los jugadores que no están expulsados ni retirados
    jugadores_disponibles = [jugador for jugador in futbolistas if not jugador.expulsado and not jugador.retirado_por_heridas]
    # Si solo hay un jugador disponible, muestra su nombre y retorna True
    if len(jugadores_disponibles) == 1:
        print(f"\n\t🏆🏆   {jugadores_disponibles[0].nombre}   🏆🏆")
        return True
    return False  # Retorna False si hay más de un jugador

def partido(futbolistas, duracion_partido):
    # Filtra los jugadores que no están expulsados ni retirados
    jugadores_disponibles = [jugador for jugador in futbolistas if not jugador.expulsado and not jugador.retirado_por_heridas]

    # Verifica si hay un único jugador disponible al inicio
    if verificar_unico_jugador(futbolistas):
        return

    duracion_primera_mitad = duracion_partido / 2  # Calcula la duración de la primera mitad
    inicio_partido = time.time()  # Marca el tiempo de inicio del partido

    print("\n\tInicia el partido.\n")
    # Ciclo para la primera mitad del partido
    while time.time() - inicio_partido < duracion_primera_mitad:
        jugadores_disponibles = [jugador for jugador in futbolistas if not jugador.expulsado and not jugador.retirado_por_heridas]
        if not jugadores_disponibles:  # Verifica si todos los jugadores están fuera
            print("Todos los jugadores han sido expulsados o se retiraron.\nPartido finalizado.")
            return

        if verificar_unico_jugador(futbolistas):  # Verifica si hay un único jugador disponible
            return

        jugador = random.choice(jugadores_disponibles)  # Selecciona un jugador aleatorio
        evento = random.choice(["gol", "lesion", "faul","patea"])  # Selecciona un evento aleatorio

        # Llama al método correspondiente según el evento
        if evento == "gol":
            jugador.hacer_gol()
        elif evento == "lesion":
            jugador.hacer_lesion()
        elif evento == "faul":
            jugador.faulear()
        elif evento == "patea":
            jugador.patear()

        time.sleep(1)  # Espera un segundo antes del siguiente evento

    print("\n\t ⏳Medio tiempo. Jugadores descansando ⏳")
    time.sleep(5)  # Simula el descanso

    print("\n\tSegunda mitad del partido.\n")
    # Ciclo para la segunda mitad del partido
    while time.time() - inicio_partido < duracion_partido:
        jugadores_disponibles = [jugador for jugador in futbolistas if not jugador.expulsado and not jugador.retirado_por_heridas]
        if not jugadores_disponibles:  # Verifica si todos los jugadores están fuera
            print("Todos los jugadores han sido expulsados o se retiraron.\nPartido finalizado")
            return

        if verificar_unico_jugador(futbolistas):  # Verifica si hay un único jugador disponible
            return

        jugador = random.choice(jugadores_disponibles)  # Selecciona un jugador aleatorio
        evento = random.choice(["gol", "lesion", "faul"])  # Selecciona un evento aleatorio

        # Llama al método correspondiente según el evento
        if evento == "gol":
            jugador.hacer_gol()
        elif evento == "lesion":
            jugador.hacer_lesion()
        elif evento == "faul":
            jugador.faulear()

        time.sleep(1)  # Espera un segundo antes del siguiente evento

    print("El tiempo ha terminado.\nPartido finalizado")

    verificar_unico_jugador(futbolistas)  # Verifica al final si hay un único jugador

# Crear jugadores y simular un partido
futbolistas = crear_jugadores()  # Llama a la función para crear jugadores
duracion_partido = 20  # Duración del partido en segundos
partido(futbolistas, duracion_partido)  # Llama a la función para simular el partido

# Mostrar estadísticas finales de los jugadores
for jugador in futbolistas:
    jugador.fichas()  # Muestra las estadísticas de cada jugador