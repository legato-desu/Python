# Diagonal de un rectangulo

import math 
"""
Crea un programa que calcule la diagonal de un rectangulo 
con la base y la altura ingresada por el usuario

Formula:
    D = raiz(b**2 + h**2)
    donde b = base y h = altura
"""
b = float(input("Ingrese la base: "))
h = float(input("Ingrese la altura: "))

d = math.sqrt(b**2 + h**2) 

print(f"La diagonal del rectangulo es: {d:.2f} cm")