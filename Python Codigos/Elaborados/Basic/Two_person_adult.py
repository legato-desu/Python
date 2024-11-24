# Two person adult
"""
Write a Program that asks the user for the age of 2 
people, and say which one is greater. Example:

- The first person is older!

If the age of both is the same, the following message is displayed:

- They are both the same age!
"""
print("\nEdad de dos personas")
print("====================\n")
person_1 = int(input("Ingrese la edad de la primer persona: "))
person_2 = int(input("Ingrese la edad de la segunda persona: "))
if person_1 == person_2:
    print("Ambos tienen la misma edad! ")
elif person_1 > person_2:
    print("La primer persona es mayor")
else:
    print("La segunda persona es mayor")        