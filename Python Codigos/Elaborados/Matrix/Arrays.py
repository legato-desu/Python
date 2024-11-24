# Arrays
"""
Create a 4x4 matrix that stores the values of a keyboard 
matrix. Prints the matrix, the fourth row, and the asterisk (*) in 
screen.
► output:
>>> IMPRIMIR matriz  : [['1','2','3','A'], ['4','5','6', 'B'],
['7','8','9', 'C'], ['*', 0, '#', 'D']]
>>> fila A IMPRIMIR  : ['*', '0', '#', 'D']
>>> DATO A IMPRIMIR  : *
"""
matrix = []
row = 3
column = 0
matrix = [['1', '2', '3', 'A'],
        ['4', '5', '6', 'B'],
        ['7', '8', '9', 'C'],
        ['*', '0', '#', 'D']]
print(">>> IMPRIMIR MATRIZ  : %s" %(matrix))
print(">>> FILA A IMPRIMIR  : %s" %(matrix[row]))
print(">>> DATO A IMPRIMIR  : %s" %(matrix[row][column]))