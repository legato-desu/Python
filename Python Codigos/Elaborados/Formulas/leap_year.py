# leap year
"""
A year is a leap year in the Gregorian calendar if it is divisible by 4 and 
not divisible by 100, and also if it is divisible by 400.
""" 
print("\nAño bisiesto")
print("============\n")
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