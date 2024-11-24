# Calcula sueldo doble

"""
Siguiendo con el ejemplo de calculo de sueldo de un empleado, ahora si el numero de 
horas trabajadas es mayor que 40 se paga al doble del valor por hora. En caso de no ser 
mayor que 40, se paga el valor de hora normal
"""
empleado = input("Ingrese el nombre del empleado: ")
horas = int(input("Numero de horas trabajadas: "))
trabajo = float(input("Valor de hora trabajada: "))

if horas <= 40:
    sueldo = horas * trabajo
else:
    sueldo = 40 * trabajo + (horas-40)*trabajo*2

print(f"Empleado {empleado.capitalize()} sueldo: ${sueldo:,.0f}")