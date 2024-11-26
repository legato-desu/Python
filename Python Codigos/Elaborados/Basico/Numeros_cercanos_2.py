# Numeros cercanos codigo compacto

"""
Escribe un programa en el que dados 5 números enteros solicitado al usuario, determine cuál de los 4 
números enteros Está más cerca del primero.
"""

number_1 = int(input("Primer numero: "))
numbers = [int(input(f"Numero {i + 2}: ")) for i in range(4)]  

subtractions = [number_1 - num for num in numbers]

minor = min(subtractions, key=lambda x: abs(x))

closest = number_1 - minor

print(f"El numero mas cercano a {number_1} es {closest}")