# Reporte clientes

"""
Una empresa vende hojas de hielo seco, con las condiciones siguientes:
        Tipo cliente            Descuento
            1                       5%
            2                       8%
            3                       12%
            4                       15%
Cuando un cliente realiza una compra se generan los siguientes datos: 
nombre del cliente, tipo de cliente, cantidad de hojas compradas, precio hoja.
Elaborar un algoritmo que permita procesar varios clientes e imprima el 
siguiente reporte:
                            Reporte clientes
        Nombre                  Subtotal        Descuento       Neto pagar
        __________________________________________________________________
        xxxxxx                  99.99            99.99          999.99
        xxxxxx                  99.99            99.99          999.99
        .
        .
        .
        xxxxxx                  99.99            99.99          999.99
        
        Total 999 Clientes      999.99           999.99         9999.99   
"""
class Reporte:
    def __init__(self,nombre,subtotal,descuento,neto):
        self.nombre = nombre
        self.subtotal = subtotal
        self.descuento = descuento
        self.neto = neto
clientes, restos, todo, descuento, total = 0,0,0,0,0
eleccion = 'S'
lista = []
def Todos():
    L = 0
    while L < len(lista):
        print(f"\t\t{lista[L].nombre}\t\t${lista[L].subtotal:,.0f}\t\t${lista[L].descuento:,.0f}\t\t${lista[L].neto:,.0f}")
        L += 1
while eleccion == 'S':
        nombre = input("Ingrese el nombre del cliente: ").capitalize()  
        tipo_cliente = int(input("Ingrese el tipo de cliente: "))
        hojas = int(input("Cuantas hojas compro?: "))
        hoja = int(input("Ingrese el precio por cada hoja: "))
        subtotal = round(hojas * hoja)
        if tipo_cliente == 1:
            descuento = subtotal * 0.05   
        elif tipo_cliente == 2:
            descuento = subtotal * 0.08
        elif tipo_cliente == 3:
            descuento = subtotal * 0.12
        elif tipo_cliente == 4:
            descuento = subtotal * 0.15
        else:
            print("Tipo de cliente no valido")
            break
        neto = subtotal - descuento
        print(f"{nombre} Subtotal: ${subtotal:,.0f} - ${descuento:,.0f} = ${neto:,.0f}")
        eleccion = input("Desea ingresar otro Cliente? (S/N): ").capitalize()
        clientes = clientes + 1
        total = total + subtotal
        restos = restos + descuento
        todo = todo + neto
        per = Reporte(nombre,subtotal,descuento,neto)
        lista.append(per)
while eleccion == 'N':
    print("\n\t\t\t\t\t\tREPORTE CLIENTES")
    print("\n\t\tNombres\t\tSubtotal\t\tDescuento\t\tNeto pagar")
    print("\t\t","-"*80)
    Todos()
    print(f"\n\t\t{clientes} Clientes\t${total:,.0f}\t\t${restos:,.0f}\t\t${todo:,.0f}")
    print("\nPrograma finalizado\n")
    break