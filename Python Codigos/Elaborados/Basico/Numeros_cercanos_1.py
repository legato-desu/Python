# Numeros cercanos

"""
Escribe un programa en el que dados 5 números enteros solicitado al usuario, determine cuál de los 4 
números enteros Está más cerca del primero.
"""

primero = int(input("Ingrese el primer numero: "))
numeros,restados = [],[]

for i in range(0,4):
    numero = int(input(f"{i+2}° Numero: "))
    numeros.append(numero)

for n in numeros:
    restados.append(primero - n)

menor = restados[0]
for r in restados:
    if abs(r) < abs(menor):
        menor = r
        
cercano = primero - menor
print(f"El numero mas cercano a {primero} es {cercano}")



# Codigo mas compacto
"""
number_1 = int(input("Primer numero: "))
numbers = [int(input(f"Numero {i + 2}: ")) for i in range(4)]  # Pedir los otros números

# Calcular las restas
subtractions = [number_1 - num for num in numbers]

# Encontrar la resta más cercana a cero (positiva o negativa)
minor = min(subtractions, key=lambda x: abs(x))

# Calcular el número más cercano
closest = number_1 - minor

print(f"El numero mas cercano a {number_1} es {closest}")
"""