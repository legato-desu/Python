# Par o impar

"""
Ingrese un número por teclado y muestre un mensaje indicando si es par o impar.
"""

number = int(input("Ingrese un numero: "))

if number == (number // 2) * 2:
    print(f"El numero {number} es par.")
else:
    print(f"El numero {number} es impar.")