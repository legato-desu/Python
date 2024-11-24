# Calcula sueldo empleado

"""
Elaborar un algoritmo que permita calcular el sueldo de un empleado, conociendo su nombre, 
número de horas trabajadas y valor de hora trabajada. 
El algoritmo debe imprimir el nombre y el sueldo. Utilizar POO. 
"""
class Empleado:
    def __init__(self, nombre, horas_trabajadas, valor_hora):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
    def sueldo(self):
        sueldo = self.horas_trabajadas * self.valor_hora
        return sueldo
    def salida(self):
        sueldo = self.sueldo()
        print(f"Empleado: {self.nombre}\nSueldo: ${sueldo:,.0f}")
nombre_empleado = input("Ingrese el nombre del empleado: ").capitalize()
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
valor_hora = float(input("Ingrese el valor de la hora trabajada: "))
empleado = Empleado(nombre_empleado, horas_trabajadas, valor_hora)
empleado.salida()