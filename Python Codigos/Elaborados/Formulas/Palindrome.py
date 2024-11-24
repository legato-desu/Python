# Palindrome
"""
Write an algorithm to determine if a word is a palindrome. 
A palindrome is a word that reads the same backwards as it does forwards.
"""
print("\nCOMPROBAR PALINDROMOS")
print("=====================\n")
chain = input("Ingresa la frase a analizar: ")
chain = chain.lower()
chain = chain.replace(' ','')
if str(chain) == str(chain)[::-1]:
    print(f"La frase - {chain} - es Palindromo")
else:
    print(f"La frase - {chain} - no es Palindromo")