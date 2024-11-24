# Guess number

import random
"""
Create a program that asks the user for a number from 1 to 50.
If the number is less say "Muy bajo" and if it is greater say "Muy alto" 
until you get the random number right.
"""
print("\nAdivina el numero")
print("=================\n")
secret = random.randint(1,50)
number = 0
while number != secret:
    number = int(input('Ingrese un numero: '))
    if number > secret:
        print('Muy alto')
        continue
    if number < secret:
        print('Muy bajo')
        continue
print('Acertaste')    