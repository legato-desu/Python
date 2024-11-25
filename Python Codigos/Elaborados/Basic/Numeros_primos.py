# Numeros primos

"""
Escribe un programa que imprima todos los números primos hasta un número ingresado por el usuario.
"""

limit = int(input("Ingrese un mumero: "))

for number in range(1, limit + 1):
    possible_cousin = True
    for divider in range(2,number):
        if number % divider == 0:
            possible_cousin = False
            break
    if possible_cousin:
            print(f"{number}",end=". ")