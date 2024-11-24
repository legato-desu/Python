# Operador basico 2

"""
Crear un programa que utilice los diferentes operadores básicos.
"""

a = 26
b = 81
c = 37

# AND
if a < b and b > c:
    print("Sentencia correcta.")
else:
    print("Sentencia no valida.")

# OR
if a > b or b < c:
    print("Sentencia correcta.")
else:
    print("Sentencia no valida.")  

# NOT
if not a > b:
    print("A es mayor que B.")
else:
    print("B es mayor que A.")