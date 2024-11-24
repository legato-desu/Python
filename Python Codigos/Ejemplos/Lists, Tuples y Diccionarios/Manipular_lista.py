# Manipular lista

"""
Crear un programa que manipule una lista de diferentes maneras.
"""

# Las listas van entre [] y se pueden modificar
list_1 = []
fruit = ["Fresa","Narajna","Mango","Pera",9,[1,2,3]]

# Posicion 5 sub lista 2
print(fruit[5][2])

# Las listas son mutables [pueden cambiar]
fruit = ["Fresa","Narajna","Mango","Pera"]

# Agregar un nuevo elemento y reemplazar la posición.
fruit[3] = "Durazno"
print(fruit)

# Las tuplas no son mutables (no cambian)
fruit = ("Fresa","Narajna","Mango","Pera")