# Conversor dias a segundos

"""
Elaborar un algoritmo  que calcule e imprima el número de segundos que hay en un determinado número de días. 
"""
dias = int(input("Ingrese la cantidad de dias: "))

segundos = dias * 60 * 60 * 24

print(f"{dias} dias tienen un totas de {segundos:,} segundos")