# Dimension matriz

"""
Cree una matriz de 3x3 que almacene los valores del 1 al 9. La el tamaño de la matriz indica el número de 
filas. Imprime cada fila de la matriz en la pantalla.

                7   8   9
            M   4   5   6   
                1   2   3   

► Salida:

>>> Matriz: [[7, 8, 9], [4, 5, 6], [7, 8, 9]]
>>> Fila 1: [7, 8, 9]
>>> Fila 2: [4, 5, 6]
>>> Fila 3: [7, 8, 9]
"""

matriz = []
length = 0
matriz = [[7, 8, 9], [4, 5, 6,], [7, 8, 9]]
length = len(matriz)
print("matriz: %s" %(matriz))
for row in range(length):
    print("Fila %d: %s" %(row+1, matriz[row]))