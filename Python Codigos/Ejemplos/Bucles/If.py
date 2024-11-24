# If

"""
Usando un if, cree una condición que compare si la variable númeroIf es positivo, negativo o 0. 
Sugerencia: los números menores que 0 son negativos y los números mayores que 0 son positivos.
"""

numberif = int(input('Ingrese el numero a evaluar: '))

if (numberif > 0):
    print(f"El numero {numberif} es positivo")
elif(numberif < 0):
    print(f"El numero {numberif} es negativo")
else:
    print(f"El numero es cero (0)")