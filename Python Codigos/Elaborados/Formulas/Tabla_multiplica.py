# Tabla de multiplicar

"""
Escriba un programa en el que al usuario se le solicite un número y Se imprime la tabla de multiplicar 
del 1 al 10 del valor introducido.
"""

number = int(input("Ingrese un numero: "))
for multiplier in range(1,11):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")