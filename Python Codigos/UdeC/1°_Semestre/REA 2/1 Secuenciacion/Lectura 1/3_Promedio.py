# Promedio estudiante

"""
Elaborar un algoritmo para calcular el promedio de calificaciones de un estudiante. 
Los datos disponibles para lectura son el nombre, el código, calificación1, calificación2, 
calificación3, y calificación4; de cada uno de los cuatro exámenes presentados. La información 
que se debe imprimir es el nombre del estudiante y el promedio de calificaciones. 
"""
estudiante = input("Ingrese el nombre del estudiante: ")

codigo = int(input("Ingrese el codigo: "))

calificacion1 = float(input("Calificacion 1: "))
calificacion2 = float(input("Calificacion 2: "))
calificacion3 = float(input("Calificacion 3: "))
calificacion4 = float(input("Calificacion 4: "))

promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4) / 4

print(f"El estudiante {estudiante.capitalize()} tuvo un promedio de: {promedio:.1f}")