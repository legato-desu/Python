# Matriz 2

import numpy as np
"""
Crear un programa que cree una matriz y la manipule.
"""

# Creamos el arreglo
a = np.array([1, 2, 3])

# Imprimimos la matriz
print(a)

# Numero de filas
print(f"Numeros de filas: {a.ndim}")

# Cantidad de arreglo
print(f"Dimencion del arreglo: {a.shape}")

# Creamos una matriz de 2D
b = np.array([(1.5, 2, 3),(4, 5, 6)],dtype = float)

# Mostramos la matriz de 2D
print(f"Matriz 2D:\n{b}\n")
print(f"Numero de filas: {b.ndim}")
print(f"Dimencion del arreglo: {b.shape}")

# Crear una matriz 3D de 2 filas x 3 columnas
c = np.array([[(1.5, 4, 3),(4, 5, 6)],[(5, 5, 5),(6, 6, 6)]])

print(f"Matriz 3D:\n{c}\n")
print(f"Numero de filas: {c.ndim}")
print(f"Dimencion del arreglo: {c.shape}")