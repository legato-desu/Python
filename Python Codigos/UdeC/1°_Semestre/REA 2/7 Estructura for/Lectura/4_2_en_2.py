# Suma los numeros pares del 2 al 160

"""
Elabora un algoritmo que calcule e imprima la suma de los numeros pares del 2 hasta el 160
Analisis del problema:
2+4+6+8+.....+160 = ?
"""
suma = 0
for i in range (0,162,2):
    suma = suma + i
print(f"{suma:.0f}")