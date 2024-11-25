# Área de un círculo

import math
"""
Programa que solicita datos al usuario para calcular el área de
un círculo (O), finalmente muestra el resultado en la pantalla.

Fórmula: Área del círculo:
área = PI*(radio**2)
"""

radius = float(input("Ingrese el radio: "))
area = math.pi*(radius**2) 
print(f"El area del circulo es: {area:.2f}(cm)²")