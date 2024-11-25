# Comprobar vocal

"""
Crea un programa para comprobar si un carácter determinado es una vocal.
c = 'i' ['a','e','i','o','u'] => true
c = 'z' ['a','e','i','o','u'] => false
"""

def es_vowel(c):

    if len(c) == 1:
        vowels = "aeiou"
        c = c.lower()
        return c in vowels

    else:
        return False

letter = input("Ingrese una vocal: ")
print(es_vowel(letter))