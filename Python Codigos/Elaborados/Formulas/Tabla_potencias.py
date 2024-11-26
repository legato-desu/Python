# Tabla de potencias

"""
Cree un código que impulse un número base del 0 al 10 y muestra el resultado de cada potencia
"""

base = int(input("Introduce el numero a elevar: "))

for exponent in range(0,10):
    power = base ** exponent
    print(f"{base}^{exponent} = {power}")