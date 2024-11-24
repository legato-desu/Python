# Student approval
"""
Create a program that receives three ratings, average them and 
say if the student passed or not
"""
print("\nAprobacion del estudiante")
print("=========================\n")
qualification_1 = float(input("Ingrese la primera calificacion: "))
qualification_2 = float(input("Ingrese la segunda calificacion: "))
qualification_3 = float(input("Ingrese la tercera calificacion: "))
average = (qualification_1 + qualification_2 + qualification_3) / 3
if average >= 3.5:
    print(f"El alumno aprobo con: {average:.1f}")
else:
    print(f"El alumno reprobo con: {average:.1f}")