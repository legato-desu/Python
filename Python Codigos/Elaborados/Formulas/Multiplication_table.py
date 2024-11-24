# Multiplication table
"""
Write a program in which the user is asked for a number and 
the multiplication table from 1 to 10 of the entered value is printed.
"""
print("\nTabla de multiplicar")
print("====================\n")
number = int(input("Ingrese un numero: "))
for multiplier in range(1,11):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")