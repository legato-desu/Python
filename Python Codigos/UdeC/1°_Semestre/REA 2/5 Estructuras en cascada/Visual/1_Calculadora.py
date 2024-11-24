# Calculadora 

"""
Crea una calculadora con valores fijos de 7 y 4 el usuario podra elegir si quiere sumar, 
restar o multiiplicar
"""
a = 7
b = 4
print(" 1. Sumar \n 2. Restar \n 3. Multiplicar")
opcion = int(input("Elige una opcion: "))
if opcion == 1:
    print(a + b)
else:
    if opcion == 2:
        print(a - b)
    else:
        if opcion == 3:
            print(a * b)   
        else:
            print("Ingreso no valido")         