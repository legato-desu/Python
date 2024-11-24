import random, time

"""
Compromiso:
    - En otro script utilice la misma clase de Futbolista y
    - crear la clase 
    ________________________
    |* EquipoFutbol        |
    |----------------------|
    |- nombre              |
    |- inversion           |
    |- extranjeros         |
    |- golesfavor          |
    |- golescontra         |
    |----------------------|
    |- comprarjugadores()  |
    |- venderjugadores()   |
    |- jugarpartido()      |
    |- recuperarlesiones() |
    |______________________|

    crear minimo 4 equipos
    crear minimo 3 jugadores por equipo
    juegan todos contra todos una sola vez
    imprimir quien gano el campeonato
    planteese retos como:
        - cuando se puede comprar un jugador
        - puedo comprar todos los jugadores que quiera
        - puedo tener mas de 3 jugadores
        - puedo tener solo goleadores o solo defensas
    todo esta en su imaginacion

    Debe presentarse con una hoja con los datos del programa, su nombre y
    la explicacion de la dinamica que diseño para este campeonato
"""

# Definimos la clase Futbolista que representa a un jugador con atributos como nombre, posición, precio, goles, lesiones y tarjetas.
class Futbolista:
    def __init__(self, nombre, posicion, precio):
        self.nombre = nombre
        self.posicion = posicion  # Goleador o Defensa
        self.precio = precio
        self.goles = 0  # Los goles empiezan en 0
        self.lesiones = random.randint(0, 2)  # Número inicial aleatorio de lesiones
        self.tamarillas = random.randint(0, 1)  # Tarjetas amarillas al inicio
        self.trojas = 0  # Las tarjetas rojas empiezan en 0
        self.expulsado = False  # Estado de expulsión
        self.retirado_por_heridas = False  # Indica si el jugador se retira por lesiones

    # Método para mostrar las estadísticas de un jugador
    def fichas(self):
        print(f"\n\t ⚽ {self.nombre} ⚽ ({self.posicion})")
        print(f" - 🥅 Goles:\t\t{self.goles}")
        print(f" - 🩺 Lesiones:\t\t{self.lesiones}")
        print(f" - 🟨 Tamarillas:\t{self.tamarillas}")
        print(f" - 🟥 Trojas:\t\t{self.trojas}")
        if self.retirado_por_heridas:
            print(f"\t{self.nombre} sale por lesiones.")

    # Método para simular que el jugador patea el balón
    def patear(self):
        print(f"El jugador {self.nombre} patea el balón")

    # Método para simular que el jugador comete una falta
    def faulear(self):
        if not self.expulsado and not self.retirado_por_heridas:
            self.tamarillas += 1  # Aumenta el número de tarjetas amarillas
            print(f"{self.nombre} ha fauleado 🟨")
            if self.tamarillas == 2:  # Si comete 2 faltas, recibe tarjeta roja
                print(f"{self.nombre} volvió a faulear 🟨🟨")
                self.recibir_roja()

    # Método para expulsar al jugador cuando recibe tarjeta roja
    def recibir_roja(self):
        self.trojas += 1
        self.expulsado = True  # Marca al jugador como expulsado
        print(f"{self.nombre} 🟥 expulsado")

    # Método para simular que el jugador anota un gol
    def hacer_gol(self):
        if not self.expulsado and not self.retirado_por_heridas:  # Solo si no está expulsado o lesionado
            self.goles += 1
            print(f"🎉 ¡Gooool de {self.nombre}!")

    # Método para simular que el jugador se lesiona
    def hacer_lesion(self):
        if not self.retirado_por_heridas:
            self.lesiones += 1  # Aumenta el número de lesiones
            print(f"{self.nombre} 🚑 lesión")
            if self.lesiones >= 3:  # Si acumula 3 o más lesiones, se retira
                print(f"{self.nombre} se retira por lesiones")
                self.retirado_por_heridas = True

# Definimos la clase EquipoFutbol que representa a un equipo con jugadores y características financieras
class EquipoFutbol:
    def __init__(self, nombre, inversion, extranjeros=0):
        self.nombre = nombre
        self.inversion = inversion  # Presupuesto del equipo
        self.extranjeros = extranjeros  # Número de jugadores extranjeros
        self.jugadores = []  # Lista de jugadores en el equipo
        self.golesfavor = 0
        self.golescontra = 0

    # Método para comprar jugadores si hay suficiente dinero y espacio en el equipo
    def comprar_jugadores(self, jugador):
        if len(self.jugadores) >= 5:
            print(f"{self.nombre} no puede tener más de 5 jugadores")
        elif self.inversion < jugador.precio:
            print(f"{self.nombre} no tiene suficiente dinero para comprar a {jugador.nombre}")
        else:
            self.jugadores.append(jugador)  # Añade al jugador al equipo
            self.inversion -= jugador.precio  # Resta el precio del jugador al presupuesto
            print(f"{self.nombre} ha comprado a {jugador.nombre} por ${jugador.precio}. Inversión restante:${self.inversion}")
            

    # Método para vender jugadores del equipo
    def vender_jugadores(self, jugador):
        if jugador in self.jugadores:
            self.jugadores.remove(jugador)  # Remueve al jugador del equipo
            self.inversion += jugador.precio  # Recupera el dinero del precio del jugador
            print(f"{jugador.nombre} ha sido vendido por {self.nombre}")
        else:
            print(f"{jugador.nombre} no está en el equipo {self.nombre}")

    # Método para jugar un partido entre dos equipos
    def jugar_partido(self, otro_equipo):
        # Filtrar jugadores disponibles (no expulsados ni retirados por lesiones)
        jugadores_disponibles = [jugador for jugador in self.jugadores if not jugador.expulsado and not jugador.retirado_por_heridas]
        otro_jugadores_disponibles = [jugador for jugador in otro_equipo.jugadores if not jugador.expulsado and not jugador.retirado_por_heridas]
        
        if not jugadores_disponibles or not otro_jugadores_disponibles:
            print("\nNo hay suficientes jugadores para el siguiente partido.")
            return None
        
        print(f"\n\t {self.nombre} VS {otro_equipo.nombre}\n")
        time.sleep(2)

        # Simula 5 eventos por partido
        for i in range(5):
            jugador = random.choice(jugadores_disponibles)
            otro_jugador = random.choice(otro_jugadores_disponibles)
            evento = random.choice(["gol", "lesion", "faul", "patear"])

            if evento == "gol":
                jugador.hacer_gol()
                self.golesfavor += 1
            elif evento == "lesion":
                jugador.hacer_lesion()
            elif evento == "faul":
                jugador.faulear()
            elif evento == 'patear':
                jugador.patear()

        # Calcula el marcador del partido
        goles_equipo1 = sum(j.goles for j in self.jugadores)
        goles_equipo2 = sum(j.goles for j in otro_equipo.jugadores)

        print(f"\n\t\tMarcador:\n\t{self.nombre} ___|{goles_equipo1} - {goles_equipo2}|___ {otro_equipo.nombre}")

        # Determina el ganador del partido
        if goles_equipo1 > goles_equipo2:
            print(f"\n\t\t🏆 {self.nombre} 🏆")
            time.sleep(2)
            return self
        elif goles_equipo1 < goles_equipo2:
            print(f"\n🏆🏆 {otro_equipo.nombre} ganó el partido")
            time.sleep(2)
            return otro_equipo
        else:
            print("\n\t\t🖐️  Empate ✋\n")
            time.sleep(2)
            return None

# Función para crear equipos y jugadores automáticamente
def crear_equipos():
    equipos = [
        EquipoFutbol("Java", inversion=100, extranjeros=2),
        EquipoFutbol("Python", inversion=80, extranjeros=1),
        EquipoFutbol("JavaScript", inversion=120, extranjeros=3),
        EquipoFutbol("Ruby", inversion=90, extranjeros=0)
    ]
    
    # Crear 3 jugadores por equipo
    for equipo in equipos:
        for i in range(3):
            jugador = Futbolista(f"Jugador {i+1} de {equipo.nombre}", random.choice(["Goleador", "Defensa"]), precio=random.randint(20, 50))
            equipo.comprar_jugadores(jugador)
    
    return equipos

# Función para jugar el campeonato
def campeonato(equipos):
    resultados = {}
    
    # Todos los equipos juegan entre sí
    for i in range(len(equipos)):
        for j in range(i+1, len(equipos)):
            ganador = equipos[i].jugar_partido(equipos[j])
            if ganador:
                if ganador.nombre in resultados:
                    resultados[ganador.nombre] += 1
                else:
                    resultados[ganador.nombre] = 1

    # Imprimir el ganador del campeonato
    ganador_campeonato = max(resultados, key=resultados.get)
    print(f"\nEl ganador del campeonato es {ganador_campeonato} con {resultados[ganador_campeonato]} victorias")
    time.sleep(5)

# Ejecución del código principal
equipos = crear_equipos()  # Crear los equipos y jugadores
campeonato(equipos)  # Iniciar el campeonato

# Mostrar estadísticas finales de los jugadores
for equipo in equipos:
    print(f"\nJugadores de {equipo.nombre}:")
    for jugador in equipo.jugadores:
        jugador.fichas()