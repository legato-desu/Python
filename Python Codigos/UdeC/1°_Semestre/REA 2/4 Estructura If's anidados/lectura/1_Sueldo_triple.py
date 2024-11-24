# Calculo sueldo triple empleado

"""
Elaborar un algoritmo similar al anterior de CALCULO DE SUELDO DOBLE DE UN EMPLEADO, 
pero ahora teniendo en cuenta que se tiene otra alternativa: las horas que exceden de 50 
se pagan al triple del valor por hora. 
"""
empleado = input("Nombre del empleado: ")
hora = float(input("Valor de horas trabajadas: "))
trabajo = float(input("Numero de horas trabajadas: "))
if trabajo <= 40:
    sueldo = hora * trabajo
elif trabajo <= 50:
    sueldo = 40 * trabajo + (hora - 40) * trabajo * 2
else:
    sueldo = 40 * trabajo + 10 * trabajo * 2 + (hora - 50 ) * trabajo * 3 
print(f"{empleado.capitalize()} tendra un sueldo de ${sueldo:,.0f}")