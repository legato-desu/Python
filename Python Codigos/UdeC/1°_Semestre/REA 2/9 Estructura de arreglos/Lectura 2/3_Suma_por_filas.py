# Suma por filas

import numpy as np
"""
Elaborar un algoritmo que lea números enteros para una matriz de 5 x 6, que imprima los elementos 
de la matriz y que al final de cada fila imprima la suma  de todos sus elementos. 
"""
matriz = np.zeros((5, 6), dtype=int)

for i in range(5):  # Filas
    for j in range(6):  # Columnas
        matriz[i, j] = int(input(f"Ingrese F{i+1} C{j+1}: "))
print(matriz)
for i in range(len(matriz)):
    fila = sum(matriz[i])
    print(f"La suma de la fila {i+1} es {fila}")