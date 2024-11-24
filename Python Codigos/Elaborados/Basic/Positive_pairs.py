# Positive pairs
"""
Create a program that prints the number of positive even numbers 
entered according to the user
k mod 2 == . => k is even
"""
print("\nNumeros pares positivos")
print("=======================\n")
def generate_even_numbers(n = 100):
    peers =[]
    counter = 0
    number = 0
    while counter < n:
        if number %2 == 0:
            peers.append(number)
            counter += 1
        number += 1
    return peers
n = int(input("Escriba la cantidad de numeros pares positivos a generar: "))
if n > 0:
    peers = generate_even_numbers(n)
    print(peers)
    print(f"Cantidad de pares: {len(peers)}")
else:
    print(f"El numero {n} es negativo")
