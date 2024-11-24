# Dice dia de la semana

"""
Elaborar un algoritmo que lea un número de día (un valor de a 1 a 7) ; e 
imprima domingo si es 1, lunes si es 2, ….., sábado si e 7.  
"""
dia = int(input("Ingresa un numero del 1 al 7: "))

match dia:
    case 1:
        print(f"El {dia}° es Domingo")
    case 2:
        print(f"El {dia}° es Lunes")
    case 3:
        print(f"El {dia}° es Martes")
    case 4:
        print(f"El {dia}° es Miercoles")
    case 5:
        print(f"El {dia}° es Jueves")
    case 6:
        print(f"El {dia}° es Viernes")
    case 7:
        print(f"El {dia}° es Sabado")
    case _:
        print("El numero no esta en el rango del 1 a 7")