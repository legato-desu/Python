# Calcula areas de figuras geometricas

from math import pi
"""
Elaborar un algoritmo que ofrezca un menú de opciones, mediante el cual se pueda escoger calcular 
el área de las figuras geométricas:
triangulo, cuadrado, rectángulo y circulo. 
Una vez seleccionada la opción, que llame a un método que permita solicitar y leer los datos necesarios,
hacer el calculo correspondiente e imprimirlo. 

AREAS DE FIGURAS GEOMETRICAS
1: TRIANGULO
2: CUADRADO
3: RECTANGULO
4: CIRCULO
5: FIN
OPCION: 
"""
class Areas:
    def triangulo(self,b,h):
        return (b * h) / 2
    def cuadrado(self,l):
        return l * l
    def rectangulo(self,b,h):
        return b * h
    def circulo(self,r):
        return (r**2)*pi 
    
def menu():
    print("\t╔═══════════════════════════════════╗\n\
        ║  AREAS DE FIGURAS GEOMETRICAS     ║\n\
        ╠═══════════════════════════════════╣\n\
        ║    1.  TRIANGULO                  ║\n\
        ║    2.  CUADRADO                   ║\n\
        ║    3.  RECTANGULO                 ║\n\
        ║    4.  CIRCULO                    ║\n\
        ║    5.  FIN                        ║\n\
        ╚═══════════════════════════════════╝")
area = Areas()
while True:
    menu()
    opcion = int(input("Opcion: "))
    if opcion == 5:
        print("Programa finalizado")
        break
    if opcion == 1:
        print("\t*** AREA DE UN TRIANGULO ***")
        print("\t\tA = b * h\n \
        \t      2")
        base = float(input("Ingrese base: "))
        altura = float(input("Ingrese altura: "))
        print(f"El area del triangulo es: {area.triangulo(base,altura):.0f} cm²")
        fin=input()
    if opcion == 2:
        print("\t*** AREA DE UN CUADRADO ***")
        print("\t\tA = L * L")
        lado = float(input("Ingrese un lado: "))
        print(f"El area del cuadrado es: {area.cuadrado(lado):.0f} cm²")
        fin = input()
    if opcion == 3:
        print("\t*** AREA DE UN RECTANGULO ***")
        print("\t\tA = b * h")
        altura = float(input("ingrese altura: "))
        base = float(input("Ingrese base: "))
        print(f"El area del rectangulo es: {area.rectangulo(base,altura):.0f} cm²")
        fin = input()
    if opcion == 4:
        print("\t*** AREA DE UN CIRCULO ***")
        print("\t\tA = π * r^2")
        radio = float(input("Ingrese radio: "))
        print(f"El area del circulo es: {area.circulo(radio):.2f} cm²")
        fin = input()