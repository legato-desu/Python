# Multiplo de tres

"""
Ingrese un número por teclado y muestre un mensaje indicando si es múltiplo de 3.
"""

number = int(input("Ingrese un numero: "))

if number == (number // 3) * 3:
    print(f"El numero {number} es multiplo de 3.")
else:
    print(f"El numero {number} no es multiplo de 3.")