# Buscar en inventario

"""
Crea un diccionario con algunas frutas y sus cantidades luego con el uso de (obtener), 
muestra la cantidad de frutas almacenadas en el inventario
"""

fruit = {
    "Peras":23,
    "Manzanas":50,
    "Sandias":7,
    "Melocotones":21,
    "Fresas":100,
    "Uvas":150,
}

search = input("Ingrese una fruta: ")
search = search.capitalize()
number = fruit.get(search,0)

print(f"hay {number} {search} en el inventario")