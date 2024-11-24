# Copia o elimina

"""
Crear un programa que copie o elimine los elementos de una lista
"""

fruit_list = ["Fresa","Naranja","Mango","Pera"]

tutor = {
    "Nombre":"David",
    "Edad":29,
    "Cursos":["Python","Java","Javascript"]
}

new_list = fruit_list.copy()
print(new_list)

new_dictionary = tutor.copy()
print(new_dictionary)

fruit_list.clear()
print(fruit_list)

tutor.clear()
print(tutor)