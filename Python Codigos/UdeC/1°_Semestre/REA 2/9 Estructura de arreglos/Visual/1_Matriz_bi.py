# Matriz bidimensional

import numpy as np
"""
Elabora un programa que lea una matriz 3x4 e imprima su matriz 
"""
matriz = np.zeros((3, 4), dtype=int)
for i in range(3):  # Filas
    for j in range(4):  # Columnas
        matriz[i, j] = int(input(f"Ingrese F{i+1} C{j+1}: "))
print(matriz)
fin = input()