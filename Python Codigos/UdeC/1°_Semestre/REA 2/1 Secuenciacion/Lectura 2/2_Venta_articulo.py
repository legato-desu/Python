# Calcula precio venta articulo

"""
Elaborar un algoritmo que calcule e imprima el precio de venta de un artículo. 
Se tiene los datos  descripción de artículo y el costo de producción. El precio de venta se 
calcula  añadiéndole al costo 120% como utilidad y el 15% de impuesto. 
"""
articulo = input("Ingrese la descripcion del articulo: ")
costo = float(input("Ingrese el costo de produccion: "))

venta = costo + costo * 1.2 + (costo + costo * 1.2) * 0.15
print(f"El articulo {articulo.capitalize()} tiene un precio de venta por: ${venta:,.0f}")