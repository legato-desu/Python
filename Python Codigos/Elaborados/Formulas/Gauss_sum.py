# Gauss sum
"""
write a program that reads a positive integer, entered by
the user and then show on the screen the sum of all the
integers from 1. The sum of the first positive integers
can be calculated in the following way:

n(n+1)
   2
"""
number = int(input("Ingrese un numero entero "))
addition = number * (number + 1 )/2
print(f"La suma desde 1 hasta {number} es {addition:.0f}")