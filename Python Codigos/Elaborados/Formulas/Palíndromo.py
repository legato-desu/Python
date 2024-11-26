# Palíndromo

"""
Escribe un algoritmo para determinar si una palabra es un palíndromo un palíndromo es una palabra que se 
lee igual hacia atrás que hacia adelante.
"""

chain = input("Ingresa la frase a analizar: ")
chain = chain.lower()
chain = chain.replace(' ','')

if str(chain) == str(chain)[::-1]:
    print(f"La frase - {chain} - es Palindromo")
else:
    print(f"La frase - {chain} - no es Palindromo")