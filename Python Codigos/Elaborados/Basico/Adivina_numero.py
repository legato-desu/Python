# Adivina el número

import random
"""
Crear un programa que pida al usuario un número del 1 al 50. Si el número es menor diga "Muy bajo" y 
si es mayor diga "Muy alto" hasta que consigas el número aleatorio correcto.
"""

secret = random.randint(1,50)
number = 0

while number != secret:
    number = int(input("Ingrese un numero: "))
    if number > secret:
        print("Muy alto")
        continue
    if number < secret:
        print("Muy bajo")
        continue

print("Acertaste")