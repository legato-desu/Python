# Promedio

"""
Cree un programa que reciba tres calificaciones, promedielas y decir si el estudiante aprobó o no
"""

notas = []
for c in range (3):
    calificacion = float(input(f"Ingrese {c+1}° calificacion: "))
    notas.append(calificacion)

promedio = sum(notas) / len(notas)

if promedio >= 3.5:
    print(f"El alumno aprobo con: {promedio:.1f}")
else:
    print(f"El alumno reprobo con: {promedio:.1f}")