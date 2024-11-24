# Increasing numbers
"""
Write a program that prints even numbers between 0 and 
200 increasing.
"""
print("Numeros pares entre 0 y 200 de forma Creciente")
for peers in range(0,201):
    if peers == int(peers/2)*2 and peers>0:
        print(peers, end=". ")