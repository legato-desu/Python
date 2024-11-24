class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.__vida = vida
        self.resistencia = self.fuerza ** 2
        self.turno = False
        self.muerto = not self.esta_vivo()

    def ver_atributos(self):
        print(f"\n*** {self.__nombre} *** ")
        print(f" - Fuerza: {self.__fuerza}")
        print(f" - Inteligencia: {self.inteligencia}")
        print(f" - Defensa: {self.defensa}")
        print(f" - Vida: {self.__vida}")
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
        if enemigo.muerto:
            if enemigo.vida == 0:
                print(enemigo.nombre, "ya estaba muerto")
            return
        
        if enemigo.esta_vivo():
            daño = self.daño(enemigo)
            enemigo.vida = round(enemigo.vida - (daño / 2))
            
            if enemigo.esta_vivo():
                print("La vida de", enemigo.nombre, "es", enemigo.vida)
            else:
                print(enemigo.nombre, "está muerto")
                enemigo.muerto = True
        else:
            print(enemigo.nombre, "ya estaba muerto")
            enemigo.muerto = True

personaje_1 = Personaje("Caballero",6,6,7,8)
personaje_2 = Personaje("Bruja",10,10,3,9)

# objetos soldado y dragon
personaje_3 = Personaje("Soldado",4,4,8,7)  
personaje_4 = Personaje("Dragon",10,10,10,10)

personaje_1.ver_atributos()
personaje_2.ver_atributos()
personaje_3.ver_atributos()
personaje_4.ver_atributos()
"""
# Ejecutar hasta que "dragon mate a soldado"
while personaje_3.esta_vivo() and personaje_4.esta_vivo():
    personaje_4.atacar(personaje_3)

print("El combate ha terminado.")

personaje_1.sabur_nivel(4,3)

print(personaje_1.esta_vivo())
personaje_1.atacar(personaje_2)

print(f"Daño: {personaje_1.daño(personaje_2)}")

while personaje_3.esta_vivo():
    
    personaje_4.atacar(personaje_3)

personaje_4.atacar(personaje_3)
"""