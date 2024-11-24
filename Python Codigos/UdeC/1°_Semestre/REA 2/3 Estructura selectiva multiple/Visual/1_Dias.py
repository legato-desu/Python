# Dia de la semana

"""
Crea un programa que por medio de una lista de numeros determinada pida uno de esos 
numeros al usuario y segun el numero le diga que dia hace referencia a ese numero 
"""
dia = int(input("Ingresa un numero del 1 al 7: "))

match dia:
    case 1:
        print(f"El {dia}° dia es Domingo")
    case 2:
        print(f"El {dia}° dia es Lunes")
    case 3:
        print(f"El {dia}° dia es Martes")
    case 4:
        print(f"El {dia}° dia es Miercoles")
    case 5:
        print(f"El {dia}° dia es Jueves")
    case 6:
        print(f"El {dia}° dia es Viernes")
    case 7:
        print(f"El {dia}° dia es Sabado")
    case _:
        print("No ingresaste un numero de 1 a 7")