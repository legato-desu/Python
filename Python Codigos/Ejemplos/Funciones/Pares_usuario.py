# Pares por usuario

"""
Crea un programa que imprima el número de números pares positivos ingresado según el usuario
k mod 2 == . => k es par
"""

def generar_pares(n = 100):
    counter, number, peers = 0, 0, []
    while counter < n:
        if number %2 == 0:
            peers.append(number)
            counter += 1
        number += 1
    return peers

n = int(input("Escriba la cantidad de numeros pares positivos a generar: "))

if n > 0:
    peers = generar_pares(n)
    print(peers)
    print(f"Cantidad de numeros pares: {len(peers)}")
else:
    print(f"El numero {n} es negativo")