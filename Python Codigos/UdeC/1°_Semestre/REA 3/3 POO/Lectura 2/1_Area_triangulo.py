# Calcula area triangulo

"""
Elaborar un algoritmo para calcular el área  de un triángulo.  
Se requiere imprimir como salida el área del triángulo. 
Los datos disponibles para leer como entrada son la base y la altura del triángulo. Utilizar POO. 
"""
class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        area = (self.base * self.altura) / 2
        return area
base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
triangulo = Triangulo(base, altura)
area = triangulo.area()
print(f"El área del triángulo es: {area}")