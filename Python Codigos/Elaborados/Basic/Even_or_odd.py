# Even or odd
"""
Enter a number by keyboard and display a message 
indicating whether it is even or odd.
"""
print("\nPar o impar")
print("===========\n")
number = int(input("Ingrese un numero: "))
if number == (number // 2) * 2:
    print(f"El numero {number} es par.")
else:
    print(f"El numero {number} es impar.")