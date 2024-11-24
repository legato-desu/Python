# Algebraic expression
"""
Create a program to Solve the algebraic expression 
(x + y ) * (x + y).
(x + y) + (x + y) = x**2 + 2xy + y**2
"""
def evaluar_expresion (x, y):
    return x**2 + 2 * x * y + y**2
print("\nExpresion algebraica")
print("====================\n")
x = float(input('Escriba el valor de x: '))
y = float(input('Escriba el valor de y: '))
print(f"Solucion: {evaluar_expresion(x, y):.0f}")