# Calcula costo intervencion pacientes hospital

"""
En un hospital se ha hecho un estudio sobre los pacientes registrados durante los últimos 10 años, 
con el objeto de Hacer una aproximación de los costos de internación por paciente. 
Se obtuvo un costo promedio diario según el tipo de enfermedad que aqueja al paciente. 
Además, se pudo determinar que en promedio todos los pacientes con edad entre 14 y 22 años 
implican un costo adicional del 10%. La siguiente tabla expresa los costos diarios, 
según el tipo de enfermedad.
    TIPO ENFERMEDAD         COSTO/PACIENTE/DIA
        1                       $250.000
        2                       $160.000
        3                       $200.000
        4                       $320.000
"""
paciente = input("Ingrese el nombre del paciiente: ")
documento = int(input("Ingrese Documento: "))
edad = int(input("Ingrese edad: "))
tipo = int(input("Tipo de enfermdad de 1 a 4: "))
dias = int(input("Ingrese el total de dias interno: "))
if tipo == 1:
    costo = dias * 250000
elif tipo == 2:
    costo = dias * 160000
elif tipo == 3:
    costo = dias * 200000
elif tipo == 4:
    costo = dias * 320000
else:
    print("Tipo de enfermedad no valida")
if edad >= 14 and edad <= 22:
    costo = costo + costo * 0.10
print(f"Paciente {paciente.capitalize()} ID:{documento} costo internacion ${costo:,.0f}")