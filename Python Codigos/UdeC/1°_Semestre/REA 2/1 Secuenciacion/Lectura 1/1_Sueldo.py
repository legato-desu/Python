# Calcula sueldo empleado

"""
Elaborar un algoritmo tal que dado como datos el nombre de un empleado, el valor de la 
hora trabajada y  número de horas trabajadas, que permita calcular su sueldo e imprima el nombre 
del empleado y su sueldo. 
"""
empleado = input("Ingrese el nombre del empleado: ")

valor_horas = int(input("Ingrese el valor de la hora trabajada: "))
total_horas = int(input("Ingrese el total de horas trabajadas: "))

sueldo = valor_horas * total_horas

print(f"El empleado {empleado.capitalize()} tendra un sueldo de: ${sueldo:,.0f}")