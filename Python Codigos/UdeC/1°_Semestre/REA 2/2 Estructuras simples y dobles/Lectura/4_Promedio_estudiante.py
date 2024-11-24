# Calcula promedio estudiante con comentario

"""
Elabora un algoritmo para calcular el promedio de calificaciones de un estudiante, los 
datos disponibles para lectura son el nombre, calificacion 1, calificacion 2, calificacion 3 y 
calificacion 4; de cada uno de los cuatro examenes presentados. La informacion que se debe 
imprimir es el nombre del estudiante, el promedio de calificaciones y un comentario de 
"Aprobado" si obtiene 3.0 o mas, o "Reprobado" en caso contrario
"""
estudiante = input("Ingrese el nombre del estudiante: ")

print("Ingrese las 4 calificaciones")

calificacion1 = float(input("Calificacion 1: "))
calificacion2 = float(input("Calificacion 2: "))
calificacion3 = float(input("Calificacion 3: "))
calificacion4 = float(input("Calificacion 4: "))

promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4) / 4

if promedio >= 3.0:
    comenraio = "APROVADO"
else:
    comenraio = "REPROBADO"

print(f"El estudiante {estudiante.capitalize()} fue {comenraio} con {promedio:.1f}")