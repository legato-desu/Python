# Date difference

from datetime import date
"""
Create a program to calculate the difference in days of two dates
"""
print("\nDiferencia de fechas")
print("====================\n")
today = date(1995,6,25)
another_day = date(2024,9,6)    
result = another_day - today
print(result)