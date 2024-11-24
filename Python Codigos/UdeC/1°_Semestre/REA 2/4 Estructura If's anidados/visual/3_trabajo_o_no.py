# Busqueda de empleo

"""
Escribir un programa que indique si una persona puede trabajar, para ello deberia: 
Estar desempleado y ser mayor de edad.
(Indica con un mensaje en caso de no cumplir alguno de los requisitos).
"""
usuario = input("Ingrese el nombre del usuario: ").capitalize()
empleo = input("Busca trabajo? (Si o No): ")

if empleo.capitalize() == "Si":
        edad = int(input("Ingrese la edad: "))
        if edad >= 18:
            print(f"{usuario} puede trabajar")
        else:
            print(f"{usuario} aun es menor de edad")
else:
    print(f"{usuario} ya tiene empleo")