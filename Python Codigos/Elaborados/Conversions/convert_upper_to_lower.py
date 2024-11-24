# Convert uppercase to lowercase
"""
Create a program that switches between upper and lower case
the words stored in the variables
"""
print("\nConvertir mayusculas a minusculas")
print("=================================\n")
small = "hola mundo"
mixed = "HOLA mundo"
big = "HOLA MUNDO"
small = small.upper() 
mixed = mixed.swapcase()  
big = big.lower() 
print(small)
print(mixed)
print(big)