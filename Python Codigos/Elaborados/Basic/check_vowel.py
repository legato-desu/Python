# Check vowel
"""
Create a program to check if a given character is a vowel.
c = 'i' ['a','e','i','o','u'] => true
c = 'z' ['a','e','i','o','u'] => false
"""
print("\nComprobar vocal")
print("===============\n")
def es_vowel(c):
    if len(c) == 1:
        vowels = 'aeiou'
        c = c.lower()
        return c in vowels
    else:
        return False
letter = input("Ingrese una vocal: ")
print(es_vowel(letter))