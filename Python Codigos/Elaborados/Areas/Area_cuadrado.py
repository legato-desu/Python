# Área de un cuadrado

"""
Programa que solicita datos al usuario para calcular el área de 
un cuadrado (▀), finalmente muestra el resultado en la pantalla.

Fórmula: Área del cuadrado
área = lado ** 2
"""

side = float(input("Ingresa un lado del cuadrado: "))
area = side ** 2
print(f"El area del cuadrado es: {area:.0f}(cm)²")