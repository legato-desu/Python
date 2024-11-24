# Area of ​​a triangle
"""
Program that asks the user for data to calculate the area of
a triangle (▲), finally display the result on the screen.

Formula: Area of the triangle
area = (base*height)/2
"""
print("\nArea de un triangulo")
print("====================\n")
a = float(input("Ingrese base: "))
h = float(input("Ingrese altura: ")) 
area = (a * h) / 2
print(f"El area del triangulo es: {area:.0f}(m)²")