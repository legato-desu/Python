# Weekday
"""
We wish to design a program that writes the names of the days of the 
week based on the value of a DAY variable entered by keyboard
"""
print("\nDias de la semana")
print("=================\n")
print("Ingresa un numero y se mostrara el dia de la semana correspondiente")
day = int(input("Ingrese un numero entre el 1 al 7: "))
match day:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _:
        print("Numero no valido")