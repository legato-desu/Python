# Fahrenheit to Celsius
"""
Program that asks the user for data to keep grades
Fahrenheit to degrees celsius.

Formula: Degrees Fahrenheit to Degrees Celsius
celsius = (Fahrenheit - 32.0) * 5.0 / 9.2
"""
print("\nFahrenheit a Celsius")
print("=====================\n")
Fahrenheit = float(input("Ingrese los grados en Fahrenheit: "))
celsius = (Fahrenheit - 32.0) * 5.0 / 9.2
print(f"{Fahrenheit:.0f}°F = {celsius:.0f}°C")