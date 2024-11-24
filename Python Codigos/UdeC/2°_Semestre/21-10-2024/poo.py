import random
import time

# Lista de nombres relacionados con conceptos de POO
nombres_jugadores = ["Abstraccion", "Polimorfismo", "Herencia", "Encapsulamiento", "Modularidad", "Clase", "Objeto", "Metodo", "Atributo", "Interfaz"]

class Futbolista:
    def __init__(self, posicion, precio):
        # Selección de un nombre aleatorio desde nombres_jugadores, o genera uno genérico si se queda sin nombres
        if nombres_jugadores:
            self.nombre = random.choice(nombres_jugadores)
            nombres_jugadores.remove(self.nombre)  # Evita nombres duplicados
        else:
            self.nombre = f"Jugador_{random.randint(100, 999)}"  # Nombre genérico
        self.posicion = posicion  
        self.precio = precio
        self.goles = 0  
        self.lesiones = random.randint(0, 2)  
        self.tamarillas = random.randint(0, 1) 
        self.trojas = 0  
        self.expulsado = False 
        self.retirado_por_heridas = False  
        self.año_retiro = set()

    def fichas(self):
        print(f"\n\t ⚽ {self.nombre} ⚽ ({self.posicion})")
        print(f" - 🥅 Goles:\t\t{self.goles}")
        print(f" - 🩺 Lesiones:\t\t{self.lesiones}")
        print(f" - 🟨 Tamarillas:\t{self.tamarillas}")
        print(f" - 🟥 Trojas:\t\t{self.trojas}")
        if self.retirado_por_heridas:
            print(f"\t{self.nombre} sale por lesiones.")

    def patear(self):
        print(f"El jugador {self.nombre} patea el balón")

    def faulear(self):
        if not self.expulsado and not self.retirado_por_heridas:
            self.tamarillas += 1  
            print(f"{self.nombre} ha fauleado 🟨")
            if self.tamarillas == 2:  
                print(f"{self.nombre} volvió a faulear 🟨🟨")
                self.recibir_roja()

    def recibir_roja(self):
        self.trojas += 1
        self.expulsado = True  
        print(f"{self.nombre} 🟥 expulsado")

    def hacer_gol(self):
        if not self.expulsado and not self.retirado_por_heridas:  
            self.goles += 1
            print(f"🎉 ¡Gooool de {self.nombre}!")

    def hacer_lesion(self):
        if not self.retirado_por_heridas:
            self.lesiones += 1  
            print(f"{self.nombre} 🚑 lesión")
            if self.lesiones >= 3:  
                print(f"{self.nombre} se retira por lesiones")
                self.retirado_por_heridas = True

    def futbolista_retirado(self):
        # Añadir un año de retiro aleatorio entre 2019 y 2024
        self.año_retiro.add(random.randint(2019, 2024))
        print(f"{self.nombre} se ha retirado en el año {list(self.año_retiro)[0]}")


class Estadio(Futbolista):
    def __init__(self, posicion, precio):
        super().__init__(posicion, precio)
        self.nombre_estadio = random.choice(["Visual Studio Code", "Console", "Notepad++", "Atom", "Sublime Text"])
        self.ubicacion = random.choice(["Windows", "Mac OS", "Linux", "Solaris", "Ubuntu"])
        self.capacidad = random.randint(15, 30)

    def mostrar_estadio(self):
        print(f"\n🏟️  Estadio: {self.nombre_estadio}")
        print(f"📍 Ubicación: {self.ubicacion}")
        print(f"👥 Capacidad: {self.capacidad} espectadores")
        print(f"\nAsociado de futbolistas: \n{self.nombre}, {self.posicion}")


class EquipoFutbol:
    def __init__(self, nombre, inversion, extranjeros=0):
        self.nombre = nombre
        self.inversion = inversion  
        self.extranjeros = extranjeros  
        self.jugadores = []  
        self.golesfavor = 0
        self.golescontra = 0

    def comprar_jugadores(self, jugador):
        if len(self.jugadores) >= 5:
            print(f"{self.nombre} no puede tener más de 5 jugadores")
        elif self.inversion < jugador.precio:
            print(f"{self.nombre} no tiene suficiente dinero para comprar a {jugador.nombre}")
        else:
            self.jugadores.append(jugador)  
            self.inversion -= jugador.precio  
            print(f"{self.nombre} ha comprado a {jugador.nombre} por ${jugador.precio}. Inversión restante: ${self.inversion}")

    def vender_jugadores(self, jugador):
        if jugador in self.jugadores:
            self.jugadores.remove(jugador)  
            self.inversion += jugador.precio 
            print(f"{jugador.nombre} ha sido vendido por {self.nombre}")
        else:
            print(f"{jugador.nombre} no está en el equipo {self.nombre}")

    def jugar_partido(self, otro_equipo):
        
        jugadores_disponibles = [jugador for jugador in self.jugadores if not jugador.expulsado and not jugador.retirado_por_heridas]
        otro_jugadores_disponibles = [jugador for jugador in otro_equipo.jugadores if not jugador.expulsado and not jugador.retirado_por_heridas]
        
        if not jugadores_disponibles or not otro_jugadores_disponibles:
            print("\nNo hay suficientes jugadores para el siguiente partido.")
            return None
        
        print(f"\n\t {self.nombre} VS {otro_equipo.nombre}\n")
        time.sleep(2)

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

        goles_equipo1 = sum(j.goles for j in self.jugadores)
        goles_equipo2 = sum(j.goles for j in otro_equipo.jugadores)

        print(f"\n\t\tMarcador:\n\t{self.nombre} ___|{goles_equipo1} - {goles_equipo2}|___ {otro_equipo.nombre}")

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

def crear_equipos():
    equipos = [
        EquipoFutbol("Java", inversion=100, extranjeros=2),
        EquipoFutbol("Python", inversion=80, extranjeros=1),
        EquipoFutbol("JavaScript", inversion=120, extranjeros=3),
        EquipoFutbol("Ruby", inversion=90, extranjeros=0)
    ]
    
    for equipo in equipos:
        for i in range(3):
            jugador = Futbolista(posicion=random.choice(["Goleador", "Defensa"]), precio=random.randint(20, 50))
            equipo.comprar_jugadores(jugador)
    
    return equipos

def campeonato(equipos):
    resultados = {}
    
    for i in range(len(equipos)):
        for j in range(i+1, len(equipos)):
            ganador = equipos[i].jugar_partido(equipos[j])
            if ganador:
                if ganador.nombre in resultados:
                    resultados[ganador.nombre] += 1
                else:
                    resultados[ganador.nombre] = 1

    ganador_campeonato = max(resultados, key=resultados.get)
    print(f"\nEl ganador del campeonato es {ganador_campeonato} con {resultados[ganador_campeonato]} victorias")
    time.sleep(5)

equipos = crear_equipos()  
campeonato(equipos)  

for equipo in equipos:
    print(f"\nJugadores de {equipo.nombre}:")
    for jugador in equipo.jugadores:
        jugador.fichas()
