# Matriz nula

"""
Haga un programa para crear una matriz nula Mmxn, donde pregunte al usuario por su dimensión m x n, 
(m son las filas y n son las columnas). Imprime cada fila de la matriz en la pantalla.
"""

length = 0
m_rows = 0
n_columns = 0
m_rows = int(input("Numero de filas (m): "))
n_columns = int(input("Numero de columnas (n): "))
M = []
for element in range(m_rows):
    M.append ([0] * n_columns)
length = len(M)
print("\nMatriz M (%dx%d): %s\n" %(m_rows,n_columns,M))
for row in range(length):
    print(M[row])