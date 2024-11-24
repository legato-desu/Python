# Ejemplo 1 de matriz 

import numpy as np
"""
Crea diferentes matrices y manipúlalas de diferentes maneras.
"""

# Matriz creada con 0 "ceros"
# ((3 "filas", 4 "columnas"))
zero = np.zeros((3,4))
print(f"Matriz identidad:\n{zero}\n")

# Arreglo creado con ciertos parámetros y 1 "unos"
# ((2 "matrices", 4 "filas", 2 "columnas"))
q = np.ones((2,4,2))
print(f"2 Matrices de unos (1) 4x2:\n{q}\n")

# Solicitamos un vector de la siguiente manera
# (rango de cero a dos, 0,2..... con 9 vectores)
t = np.linspace(0,2,9)

# Nos envía un vector con 9 elementos
print(t)
# Muestra el número de elementos de "t"
len(t)

# Creamos una matriz de 3x3 de 10 valores
f = np.full((3,3),10)
print(f)

# Matriz identidad 3x3 donde la diagonal tiene 1 (unidades)
g = np.eye(3,3)
print(g)

# Matriz con números aleatorios
h = np.random.random((10,3))
print(h)