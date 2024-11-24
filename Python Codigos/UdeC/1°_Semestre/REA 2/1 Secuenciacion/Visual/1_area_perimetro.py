# Area y Perimetro

"""
Crea un programa que calcule el area y el perimetro de un rectangulo tras ingresar la base y 
la altura por el usuario 

Formulas:
    area = b x h 
    perimetro = 2 x (b + h)
    
    donde:
    b = base y h = altura
"""
b = float(input("Ingrese la base: "))
h = float(input("Ingrese la altura: "))

area = b*h
perimetro = 2*(b+h)

print(f"El area del rectangulo es: {area:.0f} cm²")
print(f"El perimetro del rectangulo es {perimetro:.0f} cm²")