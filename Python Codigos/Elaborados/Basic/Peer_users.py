# Peer users
"""
Write a program that prints even numbers 
increasing up to a number entered by the user.
"""
number = int(input("Ingrese un numero: "))
for pair in range(0,number + 1):
    if pair == int(pair/2)*2 and pair>0:
        print(pair)