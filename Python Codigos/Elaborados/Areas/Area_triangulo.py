# Área de un triángulo

"""
Programa que solicita datos al usuario para calcular el área de
un triángulo (▲), finalmente muestra el resultado en la pantalla.

Fórmula: Área del triángulo
área = (base*altura)/2
"""

a = float(input("Ingrese base: "))
h = float(input("Ingrese altura: ")) 
area = (a * h) / 2
print(f"El area del triangulo es: {area:.0f}(cm)²")