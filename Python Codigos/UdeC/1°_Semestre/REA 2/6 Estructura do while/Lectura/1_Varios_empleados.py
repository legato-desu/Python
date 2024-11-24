# Calcula sueldo varios empleados

"""
Elaborar un algoritmo que calcule e imprima el sueldo de varios empleados, cada empleado se 
tratará en forma similar al problema de cálculo de sueldo de un empleado.
"""
eleccion = 'S'
while eleccion == 'S':
        nombre = input("Ingrese el nombre del empleado: ")
        horas = int(input("Horas trabajadas: "))
        valor_h = float(input("Valor de horas trabajadas: "))
        sueldo = round(horas * valor_h)
        print(f"{nombre} Sueldo: ${sueldo:,.0f}")
        eleccion = input("Desea ingresar otro empleado? (S) o (N): ").capitalize()
while eleccion == 'N':
        print("Programa finalizado")
        break