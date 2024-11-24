#  Conversor Ton-Kgr  y  Pies-Mts

"""
Elaborar un algoritmo tal que dado como datos el nombre de un dinosaurio, su peso  y su longitud, 
expresados estos dos últimos en toneladas y pies respectivamente; que imprima el nombre del 
dinosaurio, su peso en kilogramos y su longitud en metros. 
"""
dinosaurio = input("Ingrese el noombre del dinosaurio: ")

peso = int(input("Ingrese el peso en toneladas: "))
longitud = int(input("Ingrese longitud en pies: "))

peso_kilo = peso*1000
longitud_pies = longitud*0.32

print(f"El dinosaurio {dinosaurio.capitalize()} pesa {peso_kilo:,} kilos, con una longitud de {longitud_pies} pies" )