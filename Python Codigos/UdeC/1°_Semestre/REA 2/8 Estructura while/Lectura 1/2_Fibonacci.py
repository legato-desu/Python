# Calcula el numero 180 de la serie de fibonacci

"""
Elaborar un algoritmo que calcule el término 180 de la Serie de Fibonacci. 
Recuerde que los dos primeros números de la serie  son 0 y 1, los demás se obtienen como la suma de 
los números inmediatos que le preceden. 
0,1, 1,2, 3, 5,8,13, ……, 
"""
def fibonacci(num):
    a,b = 0,1
    for i in range(num):
        c = b+a
        a = b
        b = c
    return a
print(fibonacci(180))