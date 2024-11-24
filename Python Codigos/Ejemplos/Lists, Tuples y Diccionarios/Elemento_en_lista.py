# Elemento en lista

"""
Cree un programa donde al usuario se le solicite un país y mire si ese país es en la lista establecida o no
"""

country = input("Ingrese el nombre de el pais: ")
country = country.capitalize()

country_list = ["Peru","Brasil","Argentina","Ecuador", "Uruguay", "Chile", "Bolivia", "Colombia", "Venezuela"]

if country in country_list:
    print(f"El pais {country} si esta en la lista")
else:
    print(f"El pais {country} no esta en la lista")