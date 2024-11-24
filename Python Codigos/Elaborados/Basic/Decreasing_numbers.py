# Decreasing numbers
"""
Write a program that prints the even numbers between 0 and 
200 in descending order.
"""
print("Numeros pares entre 0 y 200 de forma decreciente")
for peers in range(200,-1,-1):
    if peers == int(peers/2)*2 and peers>0:
        print(peers, end=". ")