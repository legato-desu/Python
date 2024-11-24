# Operadores logicos

"""
Cree un programa que utilice los diferentes operadores lógicos:
and
or
not
"""

# Es verdadera si todas sn verdaderas
logic_1 = 5 > 3 and 10 > 5 and 50 > 9
print(f"'5 > 3' y '10 > 5' y '50 > 9': {logic_1}")

# Es falsa si todas son falsas
logic_2 = 1 > 3 or 10  > 5 or 50 > 9
print(f"'1 > 3' o '10  > 5' o '50 > 9': {logic_2}")

# Da el resultado opuesto
logic_3 = not 5==4
print(f"5 es diferente de 4?: {logic_3}")