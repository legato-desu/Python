# Repetir function

"""
Crear una función que dé un saludo cíclicamente según los nombres de una lista
"""

list = ["Jennifer","Mary","Bruno","David"]
def saludar(nombre,pais):
    print(f"Hola {nombre} de {pais}")

for e in range(4):
    saludar(list[e],"Quebec")