# Reporte lluvias

"""
La comisión nacional del agua, lleva un registro de las lluvias que se presentan en todas las 
poblaciones del estado, de manera que se tienen los siguientes datos: 
Población1 : XXXXXXXXXXX 
Lluvia: 99.99 
Lluvia: 99.99 
. 
. 
. 
Lluvia: 99.99             

totLluvia 999.99  

Población2 : XXXXXXXXXXX 
Lluvia: 99.99 
Lluvia: 99.99 
. 
. 
. 
Lluvia: 99.99  
. 
. 
.

Por cada población aparece el dato de lluvia tantas veces haya llovido, 
este dato está en milímetros cúbicos, pudiera darse el caso de que en 
alguna población no traiga ningún dato de lluvia, esto quiere decir 
que no llovió.  

Elaborar un algoritmo que lea estos datos e imprima el siguiente reporte: 

            REPORTE DE LLUVIAS
    POBLACION               TOTAL LLUVIA
    ------------------------------------
    xxxxxxxxxxx                 999.99
    xxxxxxxxxxx                 999.99
    .
    .
    .
    xxxxxxxxxxx                 999.99
    
    total 999 poblaciones       99999.99
    
    total poblaciones No llovio    999
    
Nota: hay la posibilidad que el estado no reporte poblacion
"""
class Reporte:
    def __init__(self,nompobla,lluvia):
        self.nompobla = nompobla
        self.lluvia = lluvia
hay = 'S'
lista = []
def Todos():
    L = 0
    while L < len(lista):
        print(f"\t\t{lista[L].nompobla}\t\t\t\t{lista[L].lluvia:.0f}")
        L += 1
totpoblaciones, tottotlluvias, totnollovio = 0, 0, 0
hay = input("Hay poblacion? (S/N): ").capitalize()
while hay == 'S':
        nompobla = input("Ingrese el nombre de la poblacion: ").capitalize()
        totlluvia = 0
        otra = input("Hay otra lluvia? (S/N): ").capitalize()
        while otra == 'S':
            lluvia = float(input("Cantidad de lluvia (milimetro cubicos): "))
            totlluvia += lluvia
            otra = input("Hay otra lluvia? (S/N): ")
        print(f"Poblacion: {nompobla}, LLuvia: {totlluvia:.0f}")
        totpoblaciones += 1
        tottotlluvias += totlluvia
        if totlluvia == 0:
            totnollovio += 1
        hay = input("Hay poblacion? (S/N): ").capitalize()
        print(f"Poblacion: {totpoblaciones}, Lluvias: {tottotlluvias}, Sin lluvia: {totnollovio}")
        reporte = Reporte(nompobla, lluvia)
        lista.append(reporte)
while hay == 'N':
    print("\n\t\t\t\tREPORTE DE LLUVIAS\n\t\tPOBLACION\t\t\tTOTAL LLUVIA")
    print("\t\t","-" * 40)
    Todos()
    print(f"\n\t\tTotal {totpoblaciones} Poblaciones\t\t\t{tottotlluvias:.0f}")
    print(f"\n\t\tTotal poblaciones no llovio\t\t{totnollovio}")
    print("\nPrograma finalizado\n")
    break