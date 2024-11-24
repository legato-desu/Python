# Calcula sueldo empleado con incentivo

"""
Siguiendo con el mismo ejemplo de calculo de sueldo de un empleado, ahora se otorga un 
incentivo de 5% del sueldo, si el empleado trabaja mas de 40 horas; es decir, al sueldo se le 
agrega el 5% del mismo sueldo
"""
empleado = input("Ingrese el nombre del empleado: ")

horas = int(input("Numero de horas trabajadas: "))
valor_hora = float(input("Valor de las horas trabajadas: "))

sueldo = horas * valor_hora

if horas >= 40:
    
    sueldo = sueldo + sueldo*0.05
    
print(f"{empleado.capitalize()} tendra un sueldo de: ${sueldo:,.0f}")