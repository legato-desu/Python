# Numeros crecientes

"""
Escriba un programa que imprima números pares entre 0 y 200 en aumento.
"""

print("Numeros pares entre 0 y 200 de forma Creciente")

for peers in range(0,201):
    if peers == int(peers/2)*2 and peers>0:
        print(peers, end=", ")