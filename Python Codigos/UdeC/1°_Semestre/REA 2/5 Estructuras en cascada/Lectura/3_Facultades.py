# Determina facultades menores

"""
Elaborar un algoritmo tal que dado como datos el código de un estudiante, la carrera en la que 
está inscrito, su semestre y su promedio; determine si el estudiante es apto para pertenecer 
a alguna de las facultades menores que tiene la universidad. Si el estudiante es aceptado 
teniendo en cuenta las especificaciones que se listan a continuación, se debe imprimir su código, 
carrera y la palabra “ACEPTADO”.
Especificaciones para pertenecer a las facultades menores:
Economía:       semestre >= 6 , promedio >=8.8
Computación:    semestre > 6 ,  promedio >=9.0
Administración: semestre > 5 ,  promedio >=8.5
Contabilidad:   semestre > 5 ,  promedio >=8.5
"""
print("     ***___ FACULTADES MENORES___***\n")
print("    Economia        Computacion \n\
    Administracion   Contabiilidad\n")
codigo = int(input("Ingrese el codigo de estudiiante: "))
carrera = input("Ingrese Carrera: ").capitalize()
semestre = int(input("Ingrese semestre: "))
promedio = float(input("Ingrese el promedio: "))
while carrera == "Economia":
    if semestre >= 6 and promedio >= 8.8:
        print(f"Estudiante {codigo} de:{carrera} fue ACEPTADO")
        break
    else:
        print("NO ACEPTADO")
        break
while carrera == "Computacion":
    if semestre > 6 and promedio >= 9.0:
        print(f"Estudiante {codigo} de:{carrera} fue ACEPTADO")
        break
    else:
        print("NO ACEPTADO")
        break
while carrera == "Administracion":
    if semestre > 5 and promedio >= 8.5:
        print(f"Estudiante {codigo} de:{carrera} fue ACEPTADO")
        break
    else:
        print("NO ACEPTADO")
        break
while carrera == "Contabilidad":
    if semestre > 5 and promedio >= 8.5:
        print(f"Estudiante {codigo} de:{carrera} fue ACEPTADO")
        break
    else:
        print("NO ACEPTADO")
        break