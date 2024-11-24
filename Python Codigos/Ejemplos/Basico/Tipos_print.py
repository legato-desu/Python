# Tipos de print

"""
Crear un programa que utilice diferentes ejemplos para mensajes en pantalla.
"""

# Uso básico de la función de impresión.
print("Este es un ejemplo basico. ")

# Se cancela el salto de línea.
print("Ejemplo sin saltar de linea. ",end="")
print("Ejemplo sin saltar de linea. ",end="")
print()

# Concatenar
print("Python ", "es ","genial")

# Se añade un (-) a los espacios.
print("Python ", "es ","genial", sep="-")
print()

# Usando la función de formato
print ("{} es {}".format("Python","genial"))

number = [2,3,5,7,11]
print(number)

capitals = {"Colombia":"Bogota","Peru":"Lima"}
print(capitals)