# Area of ​​a circle

import math
"""
Program that asks the user for data to calculate the area of
a circle (O), finally display the result on the screen.

Formula: Area of the circle:
area = PI*(radius**2)
"""
print("\nArea de un circulo")
print("==================\n")
radius = float(input("Ingrese el radio: "))
area = math.pi*(radius**2) 
print(f"El area del circulo es: {area:.2f}")