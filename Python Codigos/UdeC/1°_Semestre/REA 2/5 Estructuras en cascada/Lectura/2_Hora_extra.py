# Calcula sueldo con horas extra

"""
Elaborar un algoritmo que permita calcular lo que hay que pagarle a un trabajador teniendo en 
cuenta su sueldo y las horas extras trabajadas. Para el pago de horas extras se tiene en 
cuenta la categoría del trabajador, de acuerdo con la siguiente tabla.

Categoria       Precio hora extra
    1               $10.000
    2               $15.000
    3               $20.000
    4               $25.000
    
A los trabajadores con categoría mayor a 4 no se les pagan horas extras. 
Cada trabajador puede tener como máximo 30 horas extra, si tiene más se le pagarán 30. 
El algoritmo debe imprimir nombre del trabajador, categoría, nuevo sueldo.
"""
trabajador = input("Ingrese el nombre del trabajador: ")
categoria = int(input("Ingrese categoria: "))
sueldo = float(input("Ingrese sueldo: "))
horas = int(input("Ingrese numero de horas extra: "))
match categoria:
    case 1:
        precio = 10000
    case 2:
        precio = 15000
    case 3:
        precio = 20000
    case 4:
        precio = 25000
    case _:
        precio = 0
if horas <= 30:
    total = sueldo + horas * precio
else:
    total = sueldo + 30 * precio
print(f"El trabajador {trabajador.capitalize()} categoria {categoria} tendra un total de ${total:,.0f}")