# Specific calendar

import calendar
"""
Create a program to print the month and year requested by the user
"""
print(">>> English:")
print("\nCalendario especifico")
print("=====================\n")
year = int(input("Ingrese el año: "))
month = int(input("Ingrese el mes: "))
print(calendar.month(year, month))