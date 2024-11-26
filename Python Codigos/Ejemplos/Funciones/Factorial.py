# Factorial

"""
Escribe un algoritmo para calcular el factorial de un número. Recuerda que el factorial de un 
número n es el producto de todos los números enteros positivos de 1 a n
"""

number = int(input("Ingrese el numero para calcular su factorial: "))

def factorial(number):
    if (number ==0):
        return 1
    else:
        return number * factorial(number-1)

print(f"{number}! = {factorial(number)}")