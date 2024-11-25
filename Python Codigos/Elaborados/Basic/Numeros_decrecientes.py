# Numeros decrecientes

"""
Escriba un programa que imprima los números pares entre 0 y 200 en orden descendente.
"""

print("Numeros pares entre 0 y 200 de forma decreciente")

for peers in range(200,-1,-1):
    if peers == int(peers/2)*2 and peers>0:
        print(peers, end=", ")