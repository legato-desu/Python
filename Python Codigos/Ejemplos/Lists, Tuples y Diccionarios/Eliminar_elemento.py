# Eliminar elemento

"""
Crear un programa que elimine un elemento contenido en una lista
"""

country = ["Peru","Brasil","Argentina","Ecuador", "Uruguay", 
        "Chile", "Bolivia", "Colombia", "Venezuela"]

print(country)

# Metodo DEL
del(country[4])
print(country)

# Metodo REMOVE
country.remove("Chile")
print(country)

# Metodo POP
grd_country = country.pop(4)
print(grd_country)
print(country)