# Ayuda niño revisar operaciones fundamentales

"""
Elaborar un algoritmo  que ayude a un niño a revisar sus tareas referentes a las operaciones 
aritméticas fundamentales: sumar, restar, multiplicar y dividir.  
El proceso es el siguiente: Se ofrecerá un menú de opciones para escoger lo que desea hacer  
de acuerdo con el siguiente formato: 
TE PUEDO AYUDAR A:
1: SUMAR
2: RESTAR
3: MULTIPLICAR
4: DIVIDIR
5: FIN
OPCION: 
En caso de el niño seleccione la opción 1; está indicando que desea 
revisar operaciones de sumar, enseguida se debe establecer un proceso 
interactivo para que el niño introduzca los dos números a sumar y su resultado, 
luego que el computador le indique si la suma está correcta o incorrecta; 
en seguida le pregunte si desea revisar otra suma, si es así, 
deberá repetir todo el proceso para revisar la siguiente suma. 
Y así con las demás operaciones. 
Ejemplo:      
5 + 3 = 7       la suma es incorrecta     
5 + 3 = 8       la suma es  correcta 
"""
class AyudaNino:
    def __init__(self,n1,n2,resultado):
        self.n1 = n1
        self.n2 = n2
        self.resultado = resultado
    def sumar(self):
        total = self.n1 + self.n2
        if total == resultado:
            return True
        else:
            return False
    def restar(self):
        total = self.n1 - self.n2       
        if total == resultado:
            return True
        else:
            return False
    def multiplicar(self):
        total = self.n1 * self.n2       
        if total == resultado:
            return True
        else:
            return False
    def dividir(self):
        if self.n2 != 0:
            total = self.n1 / self.n2
            if total == resultado:
                return True
            else:
                return False
        else:
            print("No se puede dividir por cero (0)")
            return False
def menu():
    print("\t╔═══════════════════════════════════╗\n\
        ║\tLTE PUEDO AYUDAR A:         ║\n\
        ╠═══════════════════════════════════╣\n\
        ║    1.  SUMAR                      ║\n\
        ║    2.  RESTAR                     ║\n\
        ║    3.  MULTIPLICAR                ║\n\
        ║    4.  DIVIDIR                    ║\n\
        ║    5.  FIN                        ║\n\
        ╚═══════════════════════════════════╝")
while True:
    menu()
    opcion = int(input("Opcion: "))
    match opcion:
        case 1:
            while True:
                print("\t***  Te ayudo a sumar  ***")
                num1 = float(input("Primer numero: "))
                num2 = float(input("Segundo numero: "))
                resultado = float(input("Resultado: "))
                verificador = AyudaNino(num1,num2,resultado)
                if verificador.sumar():
                    print("LA SUMA ES CORRECTA")
                else:
                    print("LA SUMA ES INCORRECTA")
                repetir = input("Desea hacer otra suma? (S/N) ").capitalize()
                if repetir != 'S':
                    print("Fin de suma")
                    break
        case 2:
            while True:
                print("\t***  Te ayudo a restar  ***")
                num1 = float(input("Primer numero: "))
                num2 = float(input("Segundo numero: "))
                resultado = float(input("Resultado: "))
                verificador = AyudaNino(num1,num2,resultado)
                if verificador.restar():
                    print("LA RESTA ES CORRECTA")
                else:
                    print("LA RESTA ES INCORRECTA")
                desea = input("Desea hacer otra resta? (S/N) ").capitalize()
                if repetir != 'S':
                    print("Fin de suma")
                    break
        case 3:
            while desea == 'S':
                print("\t***  Te ayudo a multiplicar  ***")
                num1 = float(input("Primer numero: "))
                num2 = float(input("Segundo numero: "))
                resultado = float(input("Resultado: "))
                verificador = AyudaNino(num1,num2,resultado)
                if verificador.multiplicar():
                    print("LA MULTIPLICACION ES CORRECTA")
                else:
                    print("LA MULTIPLICACION ES INCORRECTA")
                desea = input("Desea hacer otra multiplicacion? (S/N) ").capitalize()
                if repetir != 'S':
                    print("Fin de suma")
                    break
        case 4:
            while desea == 'S':
                print("\t***  Te ayudo a dividir  ***")
                num1 = float(input("Primer numero: "))
                num2 = float(input("Segundo numero: "))
                resultado = float(input("Resultado: "))
                verificador = AyudaNino(num1,num2,resultado)
                if verificador.dividir():
                    print("LA DIVISION ES CORRECTA")
                else:
                    print("LA DIVISION ES INCORRECTA")
                desea = input("Desea hacer otra division? (S/N) ").capitalize()
                if repetir != 'S':
                    print("Fin de suma")
                    break
        case 5:
            print("Ayuda finalizada")
            break
        case _:
            print("Opcion no valida")