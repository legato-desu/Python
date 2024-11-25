# Funcion de sumar

"""
Cree una función con tres parámetros que sean números que se suman entre sí.
"""

def add (x, y, z):  
    return x + y + z

x = int(input("Primer numero: "))
y = int(input("Segundo numero: "))
z = int(input("Tercer numero: "))

print(f"{x} + {y} + {z} = {add(x,y,z)}")