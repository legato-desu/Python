# Calcula mayor tres numeros enteros

"""
Elaborar un algoritmo que permita leer tres números de tipo entero e imprima el mayor, 
utilizando un método para leer los números, otro método para obtener y devolver el mayor y método 
para imprimir el mayor. 
"""
def numeros():
    n1 = int(input("Ingresa el primer numero: "))
    n2 = int(input("Ingresa el segundo numero: "))
    n3 = int(input("Ingresa el tercer numero: "))
    return n1, n2, n3
def mayor(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3
def salida(final):
    print(f"El mayor es: {final}")
n1, n2, n3 = numeros()
final = mayor(n1,n2,n3)
salida(final)