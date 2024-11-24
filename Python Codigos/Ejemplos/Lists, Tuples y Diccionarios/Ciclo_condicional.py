# Ciclo condicional

"""
break: detiene o interrumpe la ejecución del bucle
continue: salta a la siguiente interacción en el bucle
"""

fruit_list = ["Fresa","Naranja","Mango","Pera"]

for fruit in fruit_list:
    if fruit == "Mango":
        continue
    print(fruit)