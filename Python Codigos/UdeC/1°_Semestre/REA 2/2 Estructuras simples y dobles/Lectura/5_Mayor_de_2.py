# Calcula mayor de dos numeros diferentes

"""
Elabora un algoritmo que lea dos numeros enteros diferenes y que calcule e imprimael mayor
"""
num_1 = int(input("Numero 1: "))
num_2 = int(input("Numero 2: "))

if num_1 == num_2:
    print("Los numeros deben ser diferentes")
elif num_1 > num_2:
    print(f"El numero {num_1} es mayor")
else:
    print(f"El numero {num_2} es mayor")