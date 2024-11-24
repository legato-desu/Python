# Upper case and lower case
"""
Write a program that asks the user for a letter and says 
whether this is UPPERCASE or lowercase.
"""
letter = input('Introduce una letra: ')
if letter <= 'z'  and letter >= 'a':  
    print(f"La letra ({letter}) es minuscula")
elif letter <= 'Z' and letter >= 'A': 
    print(f"La letra ({letter}) es mayuscula")
else:
    print(f"({letter}) No es una letra")