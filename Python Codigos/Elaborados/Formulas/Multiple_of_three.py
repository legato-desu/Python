# Multiple of three
"""
Enter a number by keyboard and display a message 
indicating if it is a multiple of 3.
"""
print("\nMultiplos del numero tres")
print("=========================\n")
number = int(input("Ingrese un numero: "))
if number == (number // 3) * 3:
    print(f"El numero {number} es multiplo de 3.")
else:
    print(f"El numero {number} no es multiplo de 3.")