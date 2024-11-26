# Matriz identidad

"""
Haga un programa que solicite un número entero positivo n y lo almacene en una variable M la matriz identidad 
n x n (la que tiene unos (1) en la diagonal principal y ceros (0) en el resto de celdas)
"""

M = []
length = 0
dimension = 0
dimension = int(input("Dimension de la matriz de tamaño n x n: "))
for element in range(dimension):
        M.append ([0] * dimension)
for row in range(dimension):
    for column in range(dimension):
        if row == column:
            M[row][column] = 1
print("\nMATRIZ M(%dx%d): %s\n" %(dimension,dimension,M))
length = len(M)
for worth in range(length):
    print(M[worth])