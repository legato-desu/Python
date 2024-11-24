# Calcula la poblacion estudiantil

"""
Una Universidad tiene actualmente 10000 estudiantes, se espera tener un crecimiento anual del 5%. 
Elaborar un algoritmo que calcule e imprima la población estudiantil que se espera tener en el año 2025
"""
estudiantes = 10000
for i in range (2021,2025,1):
    estudiantes *= (1 + 0.05)
print(f"Para 2025 se espera tener {estudiantes:,.0f} estudiantes")