# Calcule perimetro y superficie de un rectangulo

"""
Elaborar un algoritmo talque dado como datos la base y la altura  de un rectángulo, 
que calcule e imprima su perímetro y su superficie 
"""
b = float(input("Ingrese la base de el rectangulo: "))
h = float(input("Ingrese la altura de el rectangulo: "))

perimetro = 2*h + 2*b
superficie = b * h

print(f"El perimetro de el rectangulo es: {perimetro:.0f}")
print(f"La superficie de el rectangulo es: {superficie:.0f}")