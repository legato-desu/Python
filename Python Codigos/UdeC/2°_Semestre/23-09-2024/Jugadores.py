import random

class Personaje:
    def __init__(self, nombre, inteligencia):
        self.nombre = nombre
        self.fuerza = random.randint(0, 10)
        self.inteligencia = inteligencia
        self.defensa = random.randint(0, 10)
        self.vida = random.randint(0, 10)
        self.resistencia = self.fuerza ** 2
        self.turno = False
        self.muerto = not self.esta_vivo()
        self.veces_atacado = 0  # Contador de cuántas veces ha sido atacado
        
    def ver_atributos(self):
        print(f"\n*** {self.nombre} *** ")
        print(f" - Fuerza: {self.fuerza}")
        print(f" - Inteligencia: {self.inteligencia}")
        print(f" - Defensa: {self.defensa}")
        print(f" - Vida: {self.vida}")
        print(f" - Resistencia: {self.resistencia}")
        print(f" - Turno: {self.turno}")
        
    def sabur_nivel(self, fuerza, inteligencia):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        
    def esta_vivo(self):
        return self.vida > 0
    
    def daño(self, enemigo):
        return max(1, self.fuerza - enemigo.defensa)
    
    def atacar(self, enemigo):
        
        if enemigo.esta_vivo():
            daño = self.daño(enemigo)
            enemigo.vida = round(enemigo.vida - (daño / 2))
            enemigo.veces_atacado += 1  # Incrementa el contador de veces atacado
            
            if enemigo.esta_vivo():
                print(f"La vida de {enemigo.nombre} es {enemigo.vida}")
            else:
                print(f"{enemigo.nombre} está muerto")
                enemigo.muerto = True
        else:
            enemigo.muerto = True

# Crear personajes
personaje_1 = Personaje("Caballero", 6)
personaje_2 = Personaje("Bruja", 10)
personaje_3 = Personaje("Soldado", 4)  
personaje_4 = Personaje("Dragón", 10)

personaje_1.ver_atributos()
personaje_2.ver_atributos()
personaje_3.ver_atributos()
personaje_4.ver_atributos()


# Ejecutar hasta que "dragon mate a soldado"
while personaje_3.esta_vivo():
    
    personaje_4.atacar(personaje_3)

personaje_4.atacar(personaje_3)

personajes = [personaje_1, personaje_2, personaje_3, personaje_4]

# Bucle hasta que uno de los personajes muera
while all(p.esta_vivo() for p in personajes):
    for atacante in personajes:
        if not atacante.esta_vivo():
            continue
        
        # Seleccionamos un enemigo aleatorio que no sea el propio atacante y que esté vivo
        enemigos_vivos = [p for p in personajes if p != atacante and p.esta_vivo()]
        if enemigos_vivos:
            enemigo = random.choice(enemigos_vivos)
            print(f"\n{atacante.nombre} ataca a {enemigo.nombre}")
            atacante.atacar(enemigo)
        
        # Terminar si algún personaje está muerto
        if not all(p.esta_vivo() for p in personajes):
            break

print("\nEl combate ha terminado.")
print("\nResumen de ataques:")
for p in personajes:
    print(f"{p.nombre} fue atacado {p.veces_atacado} veces.")