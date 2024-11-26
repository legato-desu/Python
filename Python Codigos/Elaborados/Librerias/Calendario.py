# Calendario especifico

import calendar
"""
Crear un programa para imprimir el mes y año solicitado por el usuario
"""

year = int(input("Ingrese el año: "))
month = int(input("Ingrese el mes: "))
print(calendar.month(year, month))