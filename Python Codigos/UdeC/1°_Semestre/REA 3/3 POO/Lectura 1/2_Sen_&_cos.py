# Calcula seno y coseno

import math
"""
Elaborar un algoritmo que permita leer el tamaño de un ángulo en radianes, que calcule e 
imprima el valor del seno y del coseno. 
"""
class Angulo:
    def __init__(self, radianes):
        self.radianes = radianes
    def seno(self):
        return math.sin(self.radianes)
    def coseno(self):
        return math.cos(self.radianes)
angulo_radianes = float(input("Ingresa el tamaño del ángulo en radianes: "))
angulo = Angulo(angulo_radianes)
seno = angulo.seno()
coseno = angulo.coseno()
print(f"El seno del angulo es: {seno:.7f}")
print(f"El coseno del angulo es: {coseno:.7f}")