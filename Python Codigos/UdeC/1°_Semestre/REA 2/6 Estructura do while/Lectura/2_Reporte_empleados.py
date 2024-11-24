# Calcula sueldo varios empleados 

"""
Elabora un algoritmo que calcule e imprima el sueldo de varios empleados, cada empleado se 
tratara en forma simimlar al problema de calculo de sueldo de un empleado

En el problema anterior de sueldos de varios empleados, es necesario que los datos se 
impriman en forma de un reporte que tenga el siguiente formato. 
        REPORTE EMPLEADO
    Nombre                  Sueldo
    ______________________________
    XXXXXX                  999.99
    XXXXXX                  999.99
    -
    -
    -
    XXXXXX                  999.99
    TOTAL 99 EMPLEADOS      9999.99
"""
class Registro:
    def __init__(self,nombre,sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
empleados, salarios = 0,0
eleccion = 'S'
lista = []
def Todos():
    L = 0
    while L < len(lista):
        print(f"\t\t{lista[L].nombre}\t\t\t${lista[L].sueldo:,.0f}")
        L += 1
while eleccion == 'S':
        nombre = input("Ingrese el nombre del empleado: ").capitalize()
        horas = int(input("Horas trabajadas: "))
        valor_h = float(input("Valor de horas trabajadas: "))
        sueldo = round(horas * valor_h)
        empleados = empleados + 1
        salarios = salarios + sueldo
        per = Registro(nombre, sueldo)
        lista.append(per)
        eleccion = input("Desea ingresar otro empleado? (S) o (N): ").capitalize()
while eleccion == 'N':
    print("\t\t\tREPORTE EMPLEADOS\n\t\tNOMBRE\t\t\tSUELDO")
    print("\t\t","-" * 34)
    Todos()
    print(f"\t\t{empleados} EMPLEADOS\t\t${salarios:,.0f}")
    print("Programa finalizado")
    break