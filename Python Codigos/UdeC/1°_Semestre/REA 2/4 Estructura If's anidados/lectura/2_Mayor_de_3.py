# Calcular mayor de tres numeros

"""
Elaborar un algoritmo que lea tres números enteros diferentes, que calcule e imprima el mayor. 
Hacerlo de tres formas diferente, así: 
a. Utilizando   If then / else 
b. Utlizando    if then  y  AND 
c. Utilizando   if then/ else y AND 
"""
print("Menu de opcopnes:\n  \
        a = If then / else\n  \
        b = if then  y  AND \n  \
        c = if then/ else y AND")
opcion = input("Ingrese su opcion elegida: ").capitalize()
if opcion == "A" or  opcion == "B" or opcion == "C":
    # Utilizando  If then / else 
    while opcion == "A":
        print("OPCION A")
        num_1 = int(input("Ingrese el primer numero: "))
        num_2 = int(input("Ingrese el segundo numero: "))
        num_3 = int(input("Ingrese el tercer numero: "))
        if num_1 > num_2:
            if num_1 > num_3:
                print(f"El numero mayor es {num_1}")
            else:
                print(f"El numero mayor es {num_3}")
        elif num_2 > num_3:
            print(f"El numero mayor es {num_2}")
        else:
            print(f"El numero mayor es {num_3}")
        break
    while opcion == "B":
        print("OPCION B")
        
        num_1 = int(input("Ingrese el primer numero: "))
        num_2 = int(input("Ingrese el segundo numero: "))
        num_3 = int(input("Ingrese el tercer numero: "))
        if (num_1 > num_2) and (num_1 > num_3):
            print(f"El numero mayor es {num_1}")
        elif num_2 > num_1 and num_2 > num_3:
            print(f"El numero mayor es {num_2}")
        elif num_3 > num_1 and num_3 > num_2:
            print(f"El numero mayor es {num_3}")
        break
    while opcion == "C":
        print("OPCION C")
        num_1 = int(input("Ingrese el primer numero: "))
        num_2 = int(input("Ingrese el segundo numero: "))
        num_3 = int(input("Ingrese el tercer numero: "))
        if (num_1 > num_2) and (num_1 > num_3):
            print(f"El numero mayor es {num_1}")
        elif num_2 > num_3:
            print(f"El numero mayor es {num_2}")
        else:
            print(f"El numero mayor es {num_3}")
        break
else:
    print("Opcion no valida")