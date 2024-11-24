# Calcula el factorial de un numero

"""
Elaborar un algoritmo que lea un valor N, entero y positivo, y que calcule e imprima su factorial. 
Por ejemplo,  si se lee 5, su factorial es el producto de  5*4*3*2*1.  
El factorial de O es 1. Solución: Análisis del problema 5!= 5*4*3*2*1  
0! = 1  
"""
num = int(input("Ingrese un numero entero positivo: "))
if num > 0:
    fact = 1
    formu = ""
    for i in range (1,num+1):
        fact *= i
        formu = formu + str(i)+"x"
    formu = formu [:-1]
    print(f"{fact}! = {formu}")
elif num == 0:
    fact = 1
    print(f"{num}! = {fact}")
else:
    print("No es un numero entero positivo!")