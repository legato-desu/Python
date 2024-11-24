# Suma de matriz bidimensional 

import numpy as np
"""
Elabora un programa que lea una matriz 3x4 e imprima su matriz y la suma de cada fila y columna
"""
matriz = np.zeros((3, 4), dtype=int)
for i in range(3):  # Filas
    for j in range(4):  # Columnas
        matriz[i, j] = int(input(f"Ingrese F{i+1} C{j+1}: "))
print(matriz)
for i in range(len(matriz)):
    fila = sum(matriz[i])
    print(f"La suma de la fila {i+1} es {fila}")
for j in range(len(matriz[-1])):
    columna = 0
    for i in range(len(matriz)):
        columna += matriz[i][j]   
    print(f"La suma de la columna {j+1} es {columna}")