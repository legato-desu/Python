# Uso try

"""
Crear un programa que use (try) verificar la edad de una persona y saber si es mayor de edad
"""

age = input("Ingrese su edad: ")
try:
    age = int(age)
except:
    print("Ingrese una edad valida") 
    exit()

if age >= 18:
    print(f"Tienes {age} años, eres mayor de edad")