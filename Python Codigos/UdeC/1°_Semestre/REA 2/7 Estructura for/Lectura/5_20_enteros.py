# Calcula la suma de 20 numeros enteros

"""
Elaborar un algoritmo que lea 20 números enteros y que calcule e imprima el promedio de dichos números.
"""
suma = 0
for i in range (1,21):
    num = int(input(f"Ingrese numero {i}°: "))
    suma = suma + num
promedio = suma / 20
print(f"Total {suma}, promedio {promedio}")