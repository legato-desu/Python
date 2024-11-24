# Con el bucle for imprimir numeros

"""
Crea un programa que enseñe por pantalla un orden incrementado y otro con decremento de forma simultanea
"""
for i in range(5):
    j = 10
    for _ in range(i):
        j *= i / 2
    print(f"i:{i} - j:{j}")