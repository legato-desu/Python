# Calcula auento de sueldo segun categoria

"""
Elaborar un algoritmo tal que dado como datos el nombre, 
cédula, la categoría y el sueldo de un trabajador, que calcule el 
aumento correspondiente del sueldo, teniendo en cuenta la siguiente tabla. 

Categoria           Aumento
    1                 15%
    2                 10%
    3                 8%
    4                 7%

E imprima  el nombre, cédula,  y el nuevo sueldo. 
"""
print("Categoria           Aumento\n\
    1                 15%\n\
    2                 10%\n\
    3                 8%\n\
    4                 7%")

trabajador = input("Ingrese el nombre del trabajador: ")

cedula = int(input("Ingresa la cedula: "))
categoria = int(input("Ingrese la categoria: "))
sueldo = float(input("Ingrese el sueldo: "))

match categoria:
    case 1:
        nsueldo = sueldo + sueldo*0.15
    case 2:
        nsueldo = sueldo + sueldo*0.10
    case 3:
        nsueldo = sueldo + sueldo*0.08
    case 4:
        nsueldo = sueldo + sueldo*0.07
    case _:
        nsueldo = 0
print(f"{trabajador.capitalize()} Cc: {cedula:,} sueldo: ${nsueldo:,.0f}")