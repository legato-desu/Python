# Identity matrix
"""
Make a program that asks for a positive integer n and stores in 
a variable M the n x n identity matrix (the one with ones (1) 
on the main diagonal and zeros (0) in the rest of the cells). Print 
the matrix on the screen.

                1 0 0 0
        M    =  0 1 0 0 
                0 0 1 0
                0 0 0 1
"""
print("\nMatriz identidad")
print("================\n")
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