# Menu

"""
Cree un menú legible con opciones repetibles
"""

option = -1

while option != 3:
    print("1. Español")
    print("2. English")
    print("3. Exit")
    
    option = int(input("Ingresa una opcion: "))
    
    match option:
        case 1:
            print("Estas en español")
        case 2:
            print("There are in english")
        case 3:
            print("Exit")
        case _:
            print("Error")
            
            
"""
def menu():
    print("\t╔═══════════════════════════════════╗\n\
        ║\tLanguage\t(Idioma)    ║\n\
        ╠═══════════════════════════════════╣\n\
        ║    1.  English\t(Ingles)    ║\n\
        ║    2.  Spanish\t(Español)   ║\n\
        ║    3.  Exit\t\t(Salir)     ║\n\
        ╚═══════════════════════════════════╝")
"""