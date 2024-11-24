# Agregar metodos

"""
Crear un programa que utilice diferentes métodos para agregar un elemento.
"""

fruit_list = ["Fresa","Mango","Pera"]

fruit_dictionary = {
    "Papaya":"Naranja",
    "Uva":"Morada",
    "Guayaba":"Rosa"
}

# Diccionarios
fruit_dictionary["Fresa"]="Roja"

# Litas metodo append (x)
fruit_list.append("Sandia")

# Lista metodo insert(indice,valor)
fruit_list.insert(1,"Naranja")
print(fruit_list)