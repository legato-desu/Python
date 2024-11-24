# Calcula seno y coseno

import math
"""
Elaborar un algoritmo que permita leer el tamaño de un ángulo en radianes, luego que calcule e 
imprima el valor del seno y del coseno 
"""
angulo = float(input("Ingrese el tamaño del angulo (en radianes): "))

seno = math.sin(angulo)
coseno = math.cos(angulo)

print(f"El valor de seno es: {seno:.4f}")
print(f"El valor de coseno es: {coseno:.4f}")