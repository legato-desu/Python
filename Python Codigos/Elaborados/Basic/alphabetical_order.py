# Alphabetical order
"""
Create a (script) that prompts the user for a list of countries
separated by commas (,). These must be stored in a list.
There should not be repeated countries make use of (set). Finally,
shows the list of countries in alphabetical order via console 
and separated by commas.
"""
print("\nOrden alfabetico")
print("================\n")
items = input("Ingrese los paises separados por coma (,):\n")
paises = [pais for pais in items.split(",")]
print(",".join(sorted(list(set(paises)))))