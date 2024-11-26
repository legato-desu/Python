# texto en reversa

"""
Cree un programa que imprima la palabra inversa en la pantalla de acuerdo con 
el almacenado en la variable (cadena)
"""

cadena = input("Ingrese texto: ")

for l in range(len(cadena)-1, -1, -1):
    print(cadena[l],end='')