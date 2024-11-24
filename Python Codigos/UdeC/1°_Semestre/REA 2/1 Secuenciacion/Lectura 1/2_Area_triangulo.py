# Calcula area de un triangulo

"""
Elaborar un algoritmo para calcular el área de un triángulo. Se requiere imprimir 
como salida el área del triángulo. Los datos disponibles para lectura son la base y 
la altura del triángulo.
"""
b = float(input("Ingrese la base : "))
h = float(input("Ingrese la altura : "))

area = (b * h) / 2

print(f"El area del triangulo es: {area:.0f} cm²")