# Dimension matrix
"""
When we wanted to know the length of a list 
we used the len() function. Will it also work on 
arrays? Let's do the test.

► input:

matrix = [[1, 0], [0, 1], [0, 0]]
len(matrix)
► output:

3

It does not work correctly: it only returns the number of 
rows (which is the number of components of the list of lists that 
is the matrix). How to find out the number of columns?

► input: Function len()

matrix = [[1, 0], [0, 1], [0, 0]]
len(matrix[0])
► output:

2

___

► Statement:

Create a 3x3 matrix that stores the values 1 through 9. The 
Matrix size indicates the number of rows. Print each row 
of the matrix on the screen.

                7   8   9
            M   4   5   6   
                1   2   3   

► output:

>>> matrix: [[7, 8, 9], [4, 5, 6], [7, 8, 9]]
>>> ROW 1: [7, 8, 9]
>>> ROW 2: [4, 5, 6]
>>> ROW 3: [7, 8, 9]
"""
matrix = []
length = 0
matrix = [[7, 8, 9], [4, 5, 6,], [7, 8, 9]]
length = len(matrix)
print("matriz: %s" %(matrix))
for row in range(length):
    print("Row %d: %s" %(row+1, matrix[row]))