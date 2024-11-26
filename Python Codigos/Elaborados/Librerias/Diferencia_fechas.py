# Dias de dos fechas

from datetime import date
"""
Crear un programa para calcular la diferencia en días de dos fechas
"""


today = date(1995,6,25)
another_day = date(2024,9,6)    
result = another_day - today
print(result)