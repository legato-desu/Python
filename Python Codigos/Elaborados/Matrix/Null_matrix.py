# Null matrix
"""
Make a program to create a null matrix Mmxn, where 
ask the user for their m x n dimension, (m are the rows and n are the 
columns). Prints each row of the matrix on the screen.
                0  0  0
        M    =  0  0  0
                0  0  0
► output:
>>> MATRIZ M(3x4): [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
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