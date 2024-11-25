# Orden alfabético

"""
Cree un (script) que solicite al usuario una lista de países separados por comas (,) Estos deben 
almacenarse en una lista. No debe haber países repetidos que utilicen (conjunto). Finalmente, 
muestra la lista de países en orden alfabético a través de la consola y separados por comas.
"""

items = input("Ingrese los paises separados por coma (,):\n")
paises = [pais for pais in items.split(",")]
print(",".join(sorted(list(set(paises)))))