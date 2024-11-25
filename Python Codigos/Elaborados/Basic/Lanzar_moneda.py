# Lanzar la moneda 

import random
"""
Crea un programa para lanzar la moneda y saber si sale cara o cruz
"""

list = ["Cara"," Cruz"]
element = random.choice(list)

if element == "Cara":
    print("Ha salido cara")
else:
    print("Ha salido cruz")    