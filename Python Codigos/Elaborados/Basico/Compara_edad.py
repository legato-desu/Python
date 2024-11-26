# Two person adult

"""
Escribe un programa que solicite al usuario la edad de 2 personas y decir cuál es mayor. 

Ejemplo:
- ¡La primera persona es mayor!
Si la edad de ambos es la misma se muestra el siguiente mensaje:
- ¡Ambos tienen la misma edad!
"""

person_1 = int(input("Ingrese la edad de la primer persona: "))
person_2 = int(input("Ingrese la edad de la segunda persona: "))

if person_1 == person_2:
    print("Ambos tienen la misma edad! ")
elif person_1 > person_2:
    print("La primer persona es mayor")
else:
    print("La segunda persona es mayor")        