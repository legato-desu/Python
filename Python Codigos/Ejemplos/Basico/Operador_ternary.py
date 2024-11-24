# Operador Ternary 1

"""
Desarrollar un programa que pida al usuario un número y si es par, elevarlo al cubo, y si es impar al cuadrado
"""

number = int(input("Ingrese un numero: "))
power = number**3 if (number%2)==0 else number**2

print(f"Su resultado es: {power}")