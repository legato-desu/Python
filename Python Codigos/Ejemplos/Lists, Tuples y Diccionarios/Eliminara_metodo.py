# Eliminar metodo

"""
Crear un programa que utilice diferentes métodos para eliminar un elemento.
"""

fruit_list = ["Fresa","Mango","Pera"]

fruit_dictionary = {
    "Papaya":"Naranja",
    "Uva":"Morada",
    "Guayaba":"Rosa"
}

# Metodo pop() y popitem()..... ELIMINAR Y RETORNAR
print(fruit_list)
fruta=fruit_list.pop(1)
print(fruit_list)
print(fruta)

# Eliminar diccionario
print(fruit_dictionary)
frutas=fruit_dictionary.pop("Uva")
print(fruit_dictionary)
print(frutas)

# Metodo remove()
print(fruit_list)
fruit_list.remove("Fresa")
print(fruit_list)

# Metodo del
del fruit_dictionary ["Guayaba"]
print(fruit_list)
del fruit_list[1:3]
print(fruit_list)