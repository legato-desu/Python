# Nomina quincenal

"""
El sueldo que perciben los vendedores de una empresa automotriz, está integrado de la siguiente manera. 
El salario mínimo (quincenal), más $100000 por cada auto vendido, más el 2% del valor de los autos vendidos. 

Sueldo = SalarioMinimo + 100000*TotalAutosVendidos+ TotalVendido*0.02  

Datos que se tienen por cada vendedor: 
Nombre del vendedor: XXXXXXXXXXXXXXXX  
precioAuto: 999999.99       
precioAuto: 999999.99       
.       
.       
precioAuto: 999999.99 
Nombre del vendedor: XXXXXXXXXXXXXXXX       
precioAuto: 999999.99       
precioAuto: 999999.99       
.       
.       
precioAuto: 999999.99 
. 
. 
.  

Como se puede apreciar, se tienen varios vendedores; por cada vendedor se tiene el nombre y el 
precio de cada auto vendido en la quincena. 
Es posible que algunos vendedores  no hayan realizado venta alguna, en tal caso solo se le paga el 
salario mínimo quincenal. 
Elaborar un algoritmo que permita leer los datos  e imprimir el siguiente reporte: 

                NOMINA QUINCENAL
        NOMBRE VENDEDOR             SUELDO
        ------------------------------------
        XXXXXXXXXXXXXX              99999.99
        XXXXXXXXXXXXXX              99999.99
        .
        .
        .
        XXXXXXXXXXXXXX              99999.99
        
        TOTAL 999 VENDERORES       9999999.99
"""
class Nomina:
    def __init__(self,nomvend,sueldo):
        self.nomvend = nomvend
        self.sueldo = sueldo
eleccion = 'S'
lista = []
def Todos():
    L = 0
    while L < len(lista):
        print(f"\t\t{lista[L].nomvend}\t\t\t\t${lista[L].sueldo:,.0f}")
        L += 1
sal_min = int(input("Ingrese el salario minimo quincenal: "))
totvendedores, totsueldos = 0, 0
while eleccion == 'S':
        nomvend = input("Ingrese el nombre del vendedor: ").capitalize()
        totautos, totvendido = 0, 0
        otro = input("Hay otro auto vendido? (S/N): ").capitalize()
        while otro == 'S':
            precio_auto = int(input("Ingrese el precio del auto: "))
            totautos += 1
            totvendido += precio_auto
            otro = input("Hay otro auto vendido? (S/N): ").capitalize()
        sueldo = sal_min + 100000 * totautos + totvendido * 0.02
        print(f"{nomvend}, sueldo: ${sueldo:,.0f}")
        totvendedores += 1
        totsueldos += sueldo
        vendedores = Nomina(nomvend, sueldo)
        lista.append(vendedores)
        eleccion = input("Desea procesar otro vendedor? (S/N): ").capitalize()
while eleccion == 'N':
    print("\t\t\t\tNOMINA QUINCENAL\n\t\tNOMBRE VENDEDOR\t\t\tSUELDO")
    print("\t\t","-" * 37)
    Todos()
    print(f"\n\t\t{totvendedores} EMPLEADOS\t\t\t${totsueldos:,.0f}")
    print("\nPrograma finalizado\n")
    break