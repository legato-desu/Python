# Pares para usuario

"""
Escribe un programa que imprima números pares. aumentando hasta un número ingresado por el usuario.
"""

number = int(input("Ingrese un numero: "))

for pair in range(0,number + 1):
    if pair == int(pair/2)*2 and pair>0:
        print(pair)