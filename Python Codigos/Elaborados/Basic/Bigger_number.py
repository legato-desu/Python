# Bigger number
"""
Write a program that asks the user for 5 numbers, 
Compare them and say which one is greater.
"""
print("Ingrese 5 numeros a continuacion:")
number_1 = int(input("Primer numero: "))
number_2 = int(input("Segundo numero: "))
number_3 = int(input("Tercer numero: "))
number_4 = int(input("Cuarto numero: "))
number_5 = int(input("Quinto numero: "))
maximum = number_1
if number_2 > maximum:
    maximum = number_2
if number_3 > maximum:
    maximum = number_3
if number_4 > maximum:
    maximum = number_4
if number_5 > maximum:
    maximum = number_5
result = maximum
print(f"El numero mayor es: {result}")