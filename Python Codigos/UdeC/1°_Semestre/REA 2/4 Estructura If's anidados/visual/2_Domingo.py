# Dias semanales

"""
Escribir un programa que dado un numero indique el dia de la semana equivalente 
iniciando en Domingo = 0
"""
dia = int(input("Ingrese un numero de 0 a 6: "))

match dia:
    case 0:
        print(f"El {dia} dia es Domingo")
    case 1:
        print(f"El {dia}° dia es Lunes")
    case 2:
        print(f"El {dia}° dia es Martes")
    case 3:
        print(f"El {dia}° dia es Miercoles")
    case 4:
        print(f"El {dia}° dia es Jueves")
    case 5:
        print(f"El {dia}° dia es Viernes")
    case 6:
        print(f"El {dia}° dia es Sabado")
    case _:
        print("Numero no valido")