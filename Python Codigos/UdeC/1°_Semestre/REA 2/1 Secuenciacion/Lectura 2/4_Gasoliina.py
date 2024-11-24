# Calcula precio venta estacion de gasolina

"""
Elaborar un algoritmo  que resuelva el problema que tienen en una estación de gasolina. 
Los surtidores de la misma registran lo que “surten” en galones, pero el precio de la gasolina 
está fijado en litros. El algoritmo  debe calcular e imprimir lo que hay que cobrarle al cliente.
"""
galones = float(input("Ingrese la cantidad de galones: "))
litro = float(input("Ingrese la cantidad de litros: "))

venta = litro * 3.785*galones

print(f"El precio de venta es de ${venta:.0f}")