# Area of ​​a square
"""
Program that asks the user for data to calculate the area of 
a square (▀), finally display the result on the screen.

Formula: Area of the square
area = side ** 2
"""
print("\nArea de un cuadrado")
print("===================\n")
side = float(input("Ingresa un lado del cuadrado: "))
area = side ** 2
print(f"El area del cuadrado es: {area:.0f} cm²")