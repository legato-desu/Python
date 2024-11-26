# Ecuacion de primer grado

"""
Crea un algoritmo que te permita encontrar la solución a una ecuación de primer grado, de la 
forma: ax + b = 0 El objetivo es resolver la x y validar los datos posibles para arroja la respuesta.

Resolviendo para x tendremos que:

x = -b/a
Por tanto tendremos los siguientes escenarios:
1) Si a es DIFERENTE de 0 (a != 0) la ecuación tiene solución.
2) Si a es IGUAL a 0 (a == 0) tendremos:
Si b es DIFERENTE de 0 (b != 0) la ecuación no tiene solución.
Si b es IGUAL a 0 (b == 0) la ecuación tiene Soluciones Infinitas.
"""

a, b, x = 0, 0, 0 

a = float(input("Valor de a: "))
b = float(input("Valor de b: "))

try:
    x = -b/a
    print(f"Solucion: x = {x:.0f}")
except:
    if b != 0:
        print("La ECUACION no tiene solucion.")
    else:
        print("La ECUACION tiene infinitas soluciones.")
