# Bisiesto

"""
Un año es bisiesto en el calendario gregoriano si es divisible por 4 y no divisible por 100 y también 
si es divisible por 400.
""" 

def leap (year):
    if year % 4 != 0:
        return "El año no es bisiesto" 
    elif year % 4 == 0 and year % 100 != 0:
        return "El año es bisiesto"
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        return "El año no es bisiesto" 
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return "El año es bisiesto"

calculate = int(input("Ingrese el año a calcular (YYYY): "))
print(leap(calculate))