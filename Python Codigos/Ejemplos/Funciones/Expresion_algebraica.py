# Expresion algebraica

"""
Crea un programa para resolver la expresión algebraica.
(x + y ) * (x + y)
(x + y) + (x + y) = x**2 + 2xy + y**2
"""

def expresion (x, y):
    return x**2 + 2 * x * y + y**2

x = int(input('Escriba el valor de x: '))
y = int(input('Escriba el valor de y: '))

print(f"{x}² + 2({x})({y}) + {y}² = {expresion(x,y)}")