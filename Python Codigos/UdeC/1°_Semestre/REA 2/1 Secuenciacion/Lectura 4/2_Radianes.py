# Conversor de rad-grand y grad-rad

from math import pi
"""
Elaborar un algoritmo que permita leer un número en radianes e imprima su equivalencia en grados; 
asimismo, que permita leer un número en grados e imprima su equivalencia en radianes. 
"""
radianes = float(input('Ingrese el angulo en radianes: '))
grados = float(input('Ingrese el angulo en grados: '))

num_grados = radianes * 180 / pi
num_radianes = grados * pi / 180

print(f"{radianes:.4f} radianes, equivale a {num_grados:.0f}°")
print(f"{grados:.0f}° equivale a {num_radianes:.4f} radianes")