# Calcula promedio estudiante

"""
Elaborar un algoritmo para calcular el promedio de calificaciones de un estudiante. 
Los datos disponibles para lectura son el nombre del estudiantes, calificación 1, calificación 2 y 
calificación 3, de cada uno de los tres exámenes presentados. 
La información que se debe imprimir  es el nombre del estudiante y el promedio de calificaciones. 
Utilizar POO. 
"""
class Estudiante:
    def __init__(self, nombre, nota1, nota2, nota3):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    def promedio(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3
def datos_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    nota1 = float(input("Ingrese la calificación 1: "))
    nota2 = float(input("Ingrese la calificación 2: "))
    nota3 = float(input("Ingrese la calificación 3: "))
    return Estudiante(nombre, nota1, nota2, nota3)
def main():
    estudiante = datos_estudiante()
    promedio = estudiante.promedio()
    print(f"El promedio de {estudiante.nombre.capitalize()} es: {promedio:.1f}")
main()