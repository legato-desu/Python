# Dice vocal minuscula o vocal mayuscula 

"""
Elaborar un algoritmo tal que lea una letra e imprima 
la letra, y  si es vocal minúscula o vocal mayúscula. 
"""
vocales = ["a","i","u","e","o"]
vocal = input("Ingrese una vocal: ")

if vocal not in vocales:
    print(f"'{vocal}' esta en Mayuscula")
else:
    print(f"'{vocal}' esta en minuscula")