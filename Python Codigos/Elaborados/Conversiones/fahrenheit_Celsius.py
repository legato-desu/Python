# Fahrenheit a Celsius

"""
Programa que pide datos al usuario para mantener calificaciones
Fahrenheit a grados centígrados.

Fórmula: Grados Fahrenheit a Grados Celsius
Celsius = (Fahrenheit - 32.0) * 5.0 / 9.2
"""

Fahrenheit = float(input("Ingrese los grados en Fahrenheit: "))
celsius = (Fahrenheit - 32.0) * 5.0 / 9.2
print(f"{Fahrenheit:.0f}°F = {celsius:.0f}°C")