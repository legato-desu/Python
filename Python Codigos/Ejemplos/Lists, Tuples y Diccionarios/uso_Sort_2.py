# Uso Sort 2

"""
Crear un programa para ordenar los valores en la lista.
según sus valores "si son caracteres - alfabéticos" y si "son números - crecientes"
"""

fruit = ["Naranja","Fresa","Mango","Pera"]
numbers = {7,9,1,3,0,2,8,6,4,5}

# Sort () ordena alfabeticamente Ascendente  "reverse=True" Descendente
fruit.sort() # Ascendente
fruit.sort(reverse=True) # Descendente
print(fruit)

# Reverse()   Invierte la lista primero a ultimo y ultimo a primero
fruit.reverse()
print(fruit)

# Sorted()   Si devuelve la lista ordenada
sorted_list_1 = sorted(numbers)
sorted_list_2 = sorted(numbers,reverse=True)
print(sorted_list_1)
print(sorted_list_2)