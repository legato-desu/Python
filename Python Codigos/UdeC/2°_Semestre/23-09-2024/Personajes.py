import random

# Definimos la clase Personaje
class Personaje:
    # Inicializador de la clase Personaje
    def __init__(self, nombre, fuerza, inteligencia, defensa):
        self.nombre = nombre  # Nombre del personaje
        self.fuerza = fuerza  # Valor de la fuerza del personaje
        self.inteligencia = inteligencia  # Valor de la inteligencia del personaje
        self.defensa = defensa  # Valor de la defensa del personaje
        self.vida = random.randint(0, 10)  # Se asigna una vida aleatoria entre 0 y 10
        self.resistencia = fuerza ** 2  # La resistencia se calcula como el cuadrado de la fuerza
        self.turno = False  # Indica si es el turno del personaje, inicialmente False
        self.muerto = not self.esta_vivo()  # Verifica si el personaje está vivo al inicio
        self.veces_atacado = 0  # Contador de cuántas veces el personaje ha sido atacado
        
    # Método para mostrar los atributos del personaje
    def ver_atributos(self):
        print(f"\n*** {self.nombre} *** ")
        print(f" - Fuerza: {self.fuerza}")  # Muestra la fuerza
        print(f" - Inteligencia: {self.inteligencia}")  # Muestra la inteligencia
        print(f" - Defensa: {self.defensa}")  # Muestra la defensa
        print(f" - Vida: {self.vida}")  # Muestra la vida actual
        print(f" - Resistencia: {self.resistencia}")  # Muestra la resistencia calculada
        print(f" - Turno: {self.turno}")  # Muestra si es el turno del personaje
        
    # Método para aumentar la fuerza e inteligencia del personaje
    def sabur_nivel(self, fuerza, inteligencia):
        self.fuerza += fuerza  # Incrementa la fuerza del personaje
        self.inteligencia += inteligencia  # Incrementa la inteligencia del personaje
        
    # Método que verifica si el personaje sigue vivo
    def esta_vivo(self):
        return self.vida > 0  # Si la vida es mayor a 0, el personaje está vivo
    
    # Método para calcular el daño que inflige este personaje a un enemigo
    def daño(self, enemigo):
        return max(1, self.fuerza - enemigo.defensa)  # El daño es la fuerza menos la defensa del enemigo, con un mínimo de 1

    # Método para realizar un ataque a un enemigo
    def atacar(self, enemigo):
        if enemigo.esta_vivo():  # Solo puede atacar si el enemigo está vivo
            daño = self.daño(enemigo)  # Calcula el daño a infligir
            enemigo.vida = round(enemigo.vida - (daño / 2))  # Reduce la vida del enemigo en base al daño dividido por 2
            enemigo.veces_atacado += 1  # Incrementa el contador de veces que ha sido atacado
            
            if enemigo.esta_vivo():  # Si el enemigo sigue vivo, muestra su vida
                print(f"La vida de {enemigo.nombre} es {enemigo.vida}")
            else:
                print(f"{enemigo.nombre} ha muerto")  # Si el enemigo muere, lo marca como muerto
                enemigo.muerto = True
        else:
            enemigo.muerto = True  # Marca al enemigo como muerto si ya lo estaba

# Crear instancias de personajes
personaje_1 = Personaje("Caballero", 7, 6, 4)
personaje_2 = Personaje("Bruja", 5, 8, 6)
personaje_3 = Personaje("Soldado", 5, 6, 7)  
personaje_4 = Personaje("Dragón", 10, 8, 6)

# Mostrar atributos de cada personaje
personaje_1.ver_atributos()
personaje_2.ver_atributos()
personaje_3.ver_atributos()
personaje_4.ver_atributos()

print("")

# Lista de personajes
personajes = [personaje_1, personaje_2, personaje_3, personaje_4]

# Bucle principal para el combate
while True:
    # Verificar si algún personaje está muerto para terminar el combate
    for p in personajes:
        if not p.esta_vivo():  # Si algún personaje está muerto, el combate se detiene
            break
    else:
        # Si no hay personajes muertos, todos pueden atacar
        for atacante in personajes:
            if atacante.esta_vivo():  # Solo los personajes vivos pueden atacar
                enemigos_vivos = [p for p in personajes if p != atacante and p.esta_vivo()]  # Lista de enemigos vivos
                
                if enemigos_vivos:  # Si hay enemigos vivos, se elige uno aleatoriamente
                    enemigo = random.choice(enemigos_vivos)
                    print(f"\n{atacante.nombre} ataca a {enemigo.nombre}")
                    atacante.atacar(enemigo)  # El atacante realiza un ataque al enemigo seleccionado
            
                # Verificar si alguien ha muerto después de cada ataque
                for p in personajes:
                    if not p.esta_vivo():
                        break
        continue  # Continuar si todos siguen vivos
    break  # Terminar el combate si alguien muere

# Combate entre "Dragón" y "Soldado" hasta que el "Soldado" muera
while personaje_3.esta_vivo():
    personaje_4.atacar(personaje_3)

# Atacar una vez más para asegurar que el "Soldado" ha muerto
personaje_4.atacar(personaje_3)

print("\nEl combate ha terminado.")
print("\nResumen de ataques:")

# Mostrar cuántas veces ha sido atacado cada personaje
for p in personajes:
    print(f"{p.nombre} fue atacado {p.veces_atacado} veces.")