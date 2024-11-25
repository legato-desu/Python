# Numero mas grande

"""
Escribe un programa que pida al usuario 5 números, Compáralos y di cuál es mayor.
"""

print("Ingrese 5 numeros a continuacion:")

numeros = []
for n in range(0,5):
    number = int(input(f"{n+1}° Numero: "))
    numeros.append(number)

maximum = max(numeros)
print(f"El numero mayor es: {maximum}")