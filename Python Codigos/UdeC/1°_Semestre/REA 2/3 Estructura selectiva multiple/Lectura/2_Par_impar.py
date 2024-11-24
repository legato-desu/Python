# Dice numero par o impar entre 0 y 9

"""
Elaborar un algoritmo que lea un número entero entre 0 y 9  e 
imprima  el número y si es par o impar. 
"""
numero = int(input("Ingresa un numero entre 0 y 9: "))
if (numero % 2) == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")