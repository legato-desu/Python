# Intercambia dos numeros reales

"""
Elaborar  un algoritmo que permita leer dos números de tipo real en el método principal; 
que en un método los intercambie vía parámetros por referencia, y los imprima en el método principal. 
"""
def intercambia(a,b):
    c = a
    a = b 
    b = c
    return a, b
print("\n\t*** INTERCAMBIAR POSICION DE DOS NUMEROS ***\n")
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
print(f"\n\t1°\t2°\n\
    \t{num1}\t{num2}")
print("\t___Cambio___")
num1, num2 = intercambia(num1, num2)
print(f"\t1°\t2°\n\
    \t{num1}\t{num2}\n")
fin = input()