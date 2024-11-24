# Closest
"""
Write a program in which Given 5 integers 
requested from the user, determine which of the 4 integers 
It is closer to the first.
"""
print("\nNumero mas cercano")
print("==================\n")
print("Ingrese 5 numeros enteros a continuacion: ")
number_1 = int(input("Primer numero: "))
number_2 = int(input("Segundo numero: "))
number_3 = int(input("Tercer numero: "))
number_4 = int(input("Cuarto numero: "))
number_5 = int(input("Quinto numero: "))
subtraction_1 = number_1 - number_2
subtraction_2 = number_1 - number_3
subtraction_3 = number_1 - number_4
subtraction_4 = number_1 - number_5
minor = subtraction_1
if subtraction_2 < minor and subtraction_2 >= 0:
    minor = subtraction_2
else:
    if subtraction_2 > minor and subtraction_2 <= 0:
        minor = subtraction_2
if subtraction_3 < minor and subtraction_3 >= 0:
    minor = subtraction_3
else:
    if subtraction_3 > minor and subtraction_3 <= 0:
        minor = subtraction_3
if subtraction_4 < minor and subtraction_4 >= 0:
    minor = subtraction_4
else:
    if subtraction_4 > minor and subtraction_4 <= 0:
        minor = subtraction_4
closest = number_1 - minor
print(f"El numero mas cercano a {number_1} es {closest}")