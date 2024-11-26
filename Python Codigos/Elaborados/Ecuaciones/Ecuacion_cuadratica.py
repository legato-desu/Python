# Ecuacion cuadratica

from math import sqrt
"""
► Declaración:
Crea un algoritmo que te permita encontrar la solución a una ecuación de segundo grado, de la forma:

                    hacha**2 + bx + c = 0

Los datos del problema son los coeficientes a, b y c. es deseado calcula los valores de x que 
hacen que la ecuación sea verdadera. refranes los valores son:

x1 = -b + √ b**2 - 4ac / 2a
x2 = -b - √ b**2 - 4ac / 2a

► Consideraciones:

- En este programa debes considerar la división por cero que tiene lugar cuando a es 0 haciendo el 
denominador, 2a, nula. Cuando a es 0 la ecuación no es de segundo grado, pero primer grado.

- Otra consideración que debemos tener en cuenta es que el discriminante (b2- 4ac) no debe ser negativo, 
si es negativo el La ecuación no tiene soluciones reales.

Se deben tener en cuenta los siguientes escenarios:

1) Si a es DIFERENTE de 0 (a != 0) la ecuación tiene solución.
Si b es DIFERENTE de 0 (b! = 0) la ecuación no tiene solución.
Si b es IGUAL a 0 (b == 0), se produce la división por cero y la ecuación tiene infinitas soluciones.

"""

a, b, c = 0, 0, 0
x1, x2  = 0.0, 0.0
discriminating = 0

a = float(input("valor de a: "))
b = float(input("valor de b: "))
c = float(input("valor de c: "))

discriminating = b**2 - 4*a*c

try:
    x1 = (-b + sqrt(discriminating)) / (2 * a)
    x2 = (-b - sqrt(discriminating)) / (2 * a)
    if x1 == x2:
        print(f"Solcuion: x = {x1}")
    else:
        print(f"Solucion:\n\tx1 = {x1:.2f}\n\tx2 = {x2:.2f}")

except ZeroDivisionError:
    if b != 0:
        print("La ecuacion no tiene solucion.")
    else:
        print("La ecuacion tiene infinitas soluciones.")

except ValueError:
    print("No hay soluciones reales")
