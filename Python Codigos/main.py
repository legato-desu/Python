tup = input("Ingrese su cadena de texto: ")
cadena = tup.split()
for caracter in cadena: 
    caracter = caracter.capitalize()
    print(caracter, end=" ")