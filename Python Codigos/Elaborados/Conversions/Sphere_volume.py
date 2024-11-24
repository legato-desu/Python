# Sphere volume

from math import pi
"""
Create a program to calculate the volume of a sphere from the given radius
"""
print("\nVolumen de una esfera")
print("=====================\n")
r = float(input("Ingrese el radio de la esfera: "))
volume = 4/3 * pi * r ** 3
print(f"El volumen de una esfera con un radio de {r:.0f}cm es {volume:.2f}cm³")