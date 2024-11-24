# Calcula cambio cliente

"""
Elaborar un algoritmo talque dado el precio de un artículo vendido y la cantidad de 
dinero entregada por el cliente, que calcule e imprima el cambio que se le debe entregar al mismo
"""
articulo = float(input("Ingrese el precio del articulo: "))
cantidad = float(input("Ingrese la cantidad pagada: "))

cambio = cantidad - articulo

print(f"El cambio es de: ${cambio:,.0f}")