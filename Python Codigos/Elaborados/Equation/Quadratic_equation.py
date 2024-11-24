# Quadratic equation

from math import sqrt
"""
► Statement:
Create an Algorithm that allows you to find the solution to an equation 
of the second degree, of the form:

                    ax**2 + bx + c = 0

The data of the problem are the coefficients a, b and c. It is desired 
calculate the values of x that make the equation true. Sayings 
values are:

x1 = -b +  √ b**2 - 4ac / 2a
x2 = -b -  √ b**2 - 4ac / 2a

► Considerations:

- In this program you must consider division by zero that 
takes place when a is 0 making the denominator, 
2a, null. When a is 0 the equation is not of the second degree, 
but first degree.

- Another consideration that we must take into account is that the 
discriminant (b2- 4ac) must not be negative, if it is negative the 
equation has no real solutions.

The following scenarios must be taken into account:

1) If a is DIFFERENT from 0 (a != 0) the equation has a solution.
If b is DIFFERENT from 0 (b! = 0) the equation has no solution.
If b is EQUAL to 0 (b == 0), division by zero occurs, and the equation has infinite solutions.

► Variables
a: Main coefficient.
b: Secondary coefficient.
c: Independent Term.
x1: Unknown 1.
x2: Unknown 2.
discriminant: Discriminant of the equation.

► Test Data.
a) a = 2 , b = 7, c = 2
b) a = 1 , b = 2, c = 3
c) a = 0 , b = 2, c = 3
d) a = 0 , b = 0, c = 3

► Output:

-------------------------------------------------------
    A SECOND GRADE EQUATION: ax^2 + bx + c = 0
-------------------------------------------------------
>>> Value of a: 2
>>> Value of b: 7
>>> Value of c: 2
-------------------------------------------------------
>>> SOLUTIONS: x1 = -0.31 y x2 = -3.19
-------------------------------------------------------
"""
broad = 55
filling_1 = "-"
filling_2 = " "
empty = ""
initial_message = "ecuacion cuadratica: ax^2 + bx + c = 0"
a, b, c = 0, 0, 0
x1, x2  = 0.0, 0.0
discriminating = 0
print(empty.center(broad,filling_1))
print(initial_message.center(broad,filling_2))
print(empty.center(broad,filling_1))
a = float(input(">>> valor de a: "))
b = float(input(">>> valor de b: "))
c = float(input(">>> valor de c: "))
discriminating = b**2 - 4*a*c
try:
    x1 = (-b + sqrt(discriminating)) / (2 * a)
    x2 = (-b - sqrt(discriminating)) / (2 * a)
    print(empty.center(broad,filling_1))
    if x1 == x2:
        print(">>> SOLUCION: x = %4.2f" % x1)
    else:
        print(">>> SOLUCIONES: x1 =     %4.2f y x2 = %4.2f" % (x1, x2))
except ZeroDivisionError:
    print(empty.center(broad,filling_1))
    if b != 0:
        print("La ecuacion no tiene solucion.")
    else:
        print("La ecuacion tiene infinitas soluciones.")
except ValueError:
    print(empty.center(broad,filling_1))
    print("No hay soluciones reales")
print(empty.center(broad,filling_1))