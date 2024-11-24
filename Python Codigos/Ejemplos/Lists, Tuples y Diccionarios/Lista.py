# Lista

"""
Crear un programa que manipule los elementos de una lista.
"""

grades = [99, 90, 67, 65, 60, 98, 76, 89]

# Buscamos en la lista el valor máximo.
maximum_note = max(grades)
print(f"Valor maimo: {maximum_note}")

# Buscamos en la lista el valor mínimo.
minimum_grade = min(grades)
print(f"Valor minimo: {minimum_grade}")

# Nos fijamos en el número de valores contenidos en la lista.
note_length = len(grades)
print(f"Cantidad de valores: {note_length}")

# Ordenamos la lista de mayor a menor
sort_notes = sorted(grades)
print(f"Orden de mayor a menor: {sort_notes}")

# Ordenamos la lista en orden inverso de menor a mayor
sort_list = sorted(grades, reverse=True)
print(f"Orden de menor a mayor: {sort_list}")

# Agregue nuevos valores a la lista y muestre cuántos valores hay ahora
new_notes = grades + [90, 98, 76, 89]
print(f"Nuevos valores: {new_notes}")
print(f"Nueva cantidad de valores: {len(new_notes)}")

# Eliminamos un valor de la lista en función de su posición.
del(new_notes[0])
print(f"Nuevos valores: {new_notes}")
print(f"Nueva cantidad de valores: {len(new_notes)}")