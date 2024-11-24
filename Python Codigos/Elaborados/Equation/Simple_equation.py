# Simple equation
"""
Create an algorithm that allows you to find the solution to an equation 
of the first degree, of the form: ax + b = 0
The objective is to solve the x and validate the possible data to
throw the answer.

By solving for x we will have to:

x = -b/a
Therefore we will have the following scenarios:
1) If a is DIFFERENT from 0 (a != 0) the equation has a solution.
2) If a is EQUAL to 0 (a == 0) we will have:
If b is DIFFERENT from 0 (b != 0) the equation has no solution.
If b is EQUAL to 0 (b == 0) the equation has Infinite Solutions.

► Variables:
a: Main coefficient.
b: Independent Term.
x: Unknown.

► Test data.
a) a = 2 y b = 6.
b) a = 0 y b = 3.
c) a = 0 y b = 0.

► Output:
----------------------------------------
    ECUACION DE PRIMER GRADO: ax + b = 0  
----------------------------------------
>>> Valor de a: 2
>>> Valor de b: 6
----------------------------------------
ECUACION: 2.0 x + 6.0 = 0
----------------------------------------
>>> SOLUCION: x =  -3.0
----------------------------------------
"""
broad = 40
filling_1 = "-"
filling_2 = " "
empty = ""
initial_message = "Ecuacion de primer grado: ax + b = 0"
a = 0 
b = 0 
x = 0 
Equation_Format = "ECUACION: {} x + {} = 0"
print(empty.center(broad,filling_1))
print(initial_message.center(broad,filling_2))
print(empty.center(broad,filling_1))
a = float(input(">>> Valor de a: "))
b = float(input(">>> Valor de b: "))
print(empty.center(broad,filling_1))
print(Equation_Format.format(a,b))
print(empty.center(broad,filling_1))
try:
    x = -b/a
    print(">>> SOLUCION: x = ", x)
except:
    if b != 0:
        print("La ECUACION no tiene solucion.")
    else:
        print("La ECUACION tiene infinitas soluciones.")
print(empty.center(broad,filling_1))