# Imprime numeros del 1 al 10

"""
Elaborar un algoritmo que imprima los números enteros del 1 al 10, de tres formar diferentes 
a. Utilizando FOR 
b. Utilizando Do while 
c. Utilizando While 
"""
print("Menu de opcopnes:\n  \
        a = Utilizando FOR\n  \
        b = Utilizando Do while \n  \
        c = Utilizando While")
opcion = input("Ingrese su opcion elegida: ").capitalize()
if opcion == "A" or  opcion == "B" or opcion == "C":
    while opcion == "A":
        print("OPCION A")
        for i in range (1,11):
            print(i)
        break
    while opcion == "B":
        print("OPCION B")        
        print(f"\tPython no tiene una funcionalidad específica para crear un bucle do while\n\
            cómo otros lenguajes. Pero es posible emular un bucle do while en Python\n")
        vuelta = 1
        while True:
            print(vuelta)
            vuelta += 1
            if vuelta > 10:
                break
        break
    while opcion == "C":
        print("OPCION C")
        vuelta = 1
        while vuelta <= 10:
            print(vuelta)
            vuelta += 1
        break
else:
    print("Opcion no valida")