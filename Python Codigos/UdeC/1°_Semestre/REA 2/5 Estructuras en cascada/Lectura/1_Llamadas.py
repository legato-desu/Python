# Calcular el costo de llamadas internacionales 

"""
Elaborar  un algoritmo que permita calcular e imprimir el costo total de una llamada.
CLAVE   ZONA                PRECIO
12      América del Norte   2                   
15      América Central     2.2
18      América del Sur     4.5
19      Europa              3.5
23      Asia                6
25      África              6
29      Oceanía             5
"""
print("     CLAVE           ZONA           PRECIO \n  \
    12      América del Norte       2 \n  \
    15      América Central         2.2 \n  \
    18      América del Sur         4.5 \n  \
    19      Europa                  3.5 \n  \
    23      Asia                    6 \n  \
    25      África                  6 \n  \
    29      Oceanía                 5\n  ")
clave = int(input("Ingrese la clave: "))
minutos = int(input("Ingrese el numero de minutos: "))
match clave:
    case 12:
        costo = minutos*2
    case 15:
        costo = minutos*2.2
    case 18:
        costo = minutos*4.5
    case 19:
        costo = minutos*3.5
    case 23:
        costo = minutos*6
    case 25:
        costo = minutos*6
    case 29:
        costo = minutos*5
    case _:
        print("Codigo no valido")
print(f"Costo total de la llamada ${costo:,.0f}")