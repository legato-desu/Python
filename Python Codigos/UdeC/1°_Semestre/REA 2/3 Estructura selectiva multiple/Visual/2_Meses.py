# Meses

"""
Crea un prograa para determinar que mes es segun la inicial de dicho mes introducida por el usuario
"""
print("Digita una de estas letras")
mes = input("E, F, M, A, J: ")

match mes.capitalize():
    case "E":
        print(f"El mes ({mes}) es Enero")
    case "F":
        print(f"El mes ({mes}) es Febrero")
    case "M":
        print(f"El mes ({mes}) es Marzo")
    case "A":
        print(f"El mes ({mes}) es Abril")
    case "J":
        print(f"El mes ({mes}) es Junio")
    case _:
        print("Ingreso no valido")