# Gauss sum
"""
escribir un programa que lea un número entero positivo, ingresado por al usuario y luego mostrar en pantalla 
la suma de todos los números enteros a partir de 1. La suma de los primeros números enteros positivos
se puede calcular de la siguiente manera:

n(n+1)
   2
"""

number = int(input("Ingrese un numero entero "))
addition = number * (number + 1 )/2
print(f"La suma desde 1 hasta {number} es {addition:.0f}")