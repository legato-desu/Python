# Calcula area y volumen de un cilindro

from math import pi
"""
Elaborar un algoritmo talque dado como datos el radio y la altura de un cilindro. 
Que calcule e imprima el área y su volumen.
"""
radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

area = 2 * pi * radio * altura
volumen = 2*pi * radio*(radio+altura)

print(f"El area del cilindro es: {area:3f}")
print(f"El volumen del cilinndro es: {volumen:3f}")