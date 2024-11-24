# Print beautifully

import pprint
"""
Use of the -pprint- library to print in an orderly manner and 
nice code
"""
class Vehicle:
    """ Inicia atributos color,ruedas,puertas """
    def __init__(self, color, wheels, doors):
        self.color = color
        self.wheels = wheels
        self.doors = doors
    """ Simulacion para mostrar por consola """
    def characteristics(self):
        print("color:", self.color, ",ruedas:", self.wheels, ",puertas:", self.doors)    
class Car(Vehicle):
    def __init__(self, color, wheels, doors,speed,displacement):
        super().__init__(color, wheels, doors)
        self.speed = speed
        self.displacement = displacement
    def characteristics(self):
        super().characteristics()
        print("velocidad:",self.speed,"km/h","Cilindrada",self.displacement,"cc")
""" Asignar valores a la clase Coche y su herencia y enseñar por consola """
print("")
c1 = Car("negro","4","5","80","1.000")
c1.characteristics()
print("")
c2 = Car("gris","4","3","100","1.300")
c2.characteristics()