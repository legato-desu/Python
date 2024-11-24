# Tabla conversion grados fagrenheit a celsius

"""
Una temperatura en grados Fahrenheit se convierte a grados Celsius, con la siguiente ecuación 
C=5/9*(F -32). Elaborar un algoritmo que imprima una tabla desde 1 hasta 65 ( con intervalos de 1) 
grados Fahrenheit con sus equivalencias en grados Celsius.
        Fahrenheit       Celsius
        ________________________
            1             99.99
            2             99.99
            3             99.99
            .
            .
            .
            65            99.99
"""
def Tabla():
    print("\t\tFahrenheit\tCelsius")
    print("\t","-" * 32)
    for f in range (0,66,1):
        c = (f-32)*5/9
        print(f"\t\t{f}°\t\t{c:.2f}°")
Tabla()