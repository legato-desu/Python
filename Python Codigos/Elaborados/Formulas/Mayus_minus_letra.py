# Mayuscula o minuscula

"""
Escriba un programa que pida al usuario una carta y diga ya sea MAYÚSCULAS o minúsculas.
"""

letter = input('Introduce una letra: ')

if letter <= 'z'  and letter >= 'a':  
    print(f"La letra ({letter}) es minuscula")
elif letter <= 'Z' and letter >= 'A': 
    print(f"La letra ({letter}) es mayuscula")
else:
    print(f"({letter}) No es una letra")