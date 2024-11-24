# Retirement
"""
Ask the user for their age and gender, so that the computer can tell them 
If you can retire now. Take into account that a Man can retire 
when she is 60 years old or older, on the other hand, an older woman 
You will retire if you are over 54 years old.
"""
gender = input("Ingrese M para Masculino o F para Femenino: ")
age= int(input("Ingrese la edad: "))
gender = gender.capitalize()
if gender == "M":
    if age >= 60:
        print("Puede jubilarse")
    else:
        print("No puede jubilarse")
elif gender == "F":
    if age >= 54:
        print("Puede jubilarse")
    else:
        print("No puede jubilarse")
else:
    print("Digite una de las opciones validas de genero (M o F)")            