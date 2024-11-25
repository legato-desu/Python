# Histograma

"""
Crear un programa para hacer un histograma a partir de una lista de números enteros
Análisis:
[2, 1, 5, 3]
* *
*
* * * * *
* * *
"""

rango = int(input("Cuantos numeros va a ingresar?: "))

numeros = []
for r in range(rango):
    numero = int(input(f"{r+1}° Numero: "))
    numeros.append(numero)

def histograma (numeros, caracter ='* '):
    for h in numeros:
        print(caracter * h)

histograma(numeros)