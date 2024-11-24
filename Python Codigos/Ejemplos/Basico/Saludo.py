# Saludo

"""
Escriba un programa que solicite el nombre y apellido del usuario. Después de que los datos de la 
muestra hayan sido ingresados en la pantalla, cadena 'Hola {nombre} {apellido}, ¡encantado de conocerlo!
"""

name = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")

print(f"¡Hola {name.capitalize()} {last_name.capitalize()}, ¡encantado de conocerlo!")