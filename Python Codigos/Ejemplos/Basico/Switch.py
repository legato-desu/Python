# Switch

"""
Crea un programa que pida al usuario un número del 1 al 4 y lo muestre en pantalla. 
¿A qué estación corresponde ese número?
"""

season = int(input("Ingrese un numero de 1 a 4: "))
match season:
    case 1:
        print(f"La {season}° estacion es: Primavera")
    case 2:
        print(f"La {season}° estacion es: Verano")
    case 3:
        print(f"La {season}° estacion es: Otoño")
    case 4:
        print(f"La {season}° estacion es: Invierno")
    case _:
        print(f" {season} No es un numero valido")