# Inventory Search
"""
Create a dictionary with some fruits and their quantities then with the 
use of (get), show the amount of fruits as stored in The inventory
"""
print("\nBusqueda de inventario")
print("======================\n")
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