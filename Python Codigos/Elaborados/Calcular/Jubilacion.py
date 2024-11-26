# Retirement

"""
Preguntar al usuario su edad y sexo, para que el ordenador pueda decírselo. 
Si puedes jubilarte ahora. Toma en cuenta que un Hombre puede jubilarse cuando tiene 60 años o más, 
en cambio, una mujer mayor Te jubilarás si tienes más de 54 años.
"""

gender = input("Ingrese M para Masculino o F para Femenino: ").capitalize()
age= int(input("Ingrese la edad: "))

if gender == "M":
    if age >= 60:
        print(f"Tiene {age} años y puede jubilarse")
    else:
        print(f"Tiene {age} años y no puede jubilarse")
elif gender == "F":
    if age >= 54:
        print(f"Tiene {age} años y puede jubilarse")
    else:
        print(f"Tiene {age} años y no puede jubilarse")
else:
    print("Digite una de las opciones validas de genero (M o F)")            