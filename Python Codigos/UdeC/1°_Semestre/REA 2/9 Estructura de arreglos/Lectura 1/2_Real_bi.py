# Captura e imprime numeros reales en arreglo bidimensional}

import numpy as np
"""
Elaborar un algoritmo que capture números reales en una matriz 
de 3x4  y que lo imprima
"""
matriz = np.zeros((3, 4), dtype=float)
for i in range(3):  # Filas
    for j in range(4):  # Columnas
        matriz[i, j] = float(input(f"Ingrese F{i+1 } C{j+1}: "))
print(matriz)