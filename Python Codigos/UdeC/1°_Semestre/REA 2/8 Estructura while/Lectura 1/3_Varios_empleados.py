# Calcula sueldo de varios empleados

"""
Elaborar un algoritmo que permita procesar varios empleados, igual al primer ejemplo de Do while 
pero con la posibilidad que No se procese ningún empleado (o que No se realice el ciclo repetitivo) 
"""
eleccion = input("Deseia procesar otro empleado? (S/N) ")
while eleccion.capitalize() == 'S':
    nombre = input("Ingrese el nombre del empleado: ")
    horas = int(input("Total de horas trabajadas: "))
    valor = int(input("Valor de cada hora: "))
    sueldo = horas * valor
    print(f"{nombre.capitalize()} sueldo de: ${sueldo:,.0f}")
    eleccion = input("Deseia procesar otro empleado? (S/N) ")