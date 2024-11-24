# Encapsulamiento

"""
Para practicar la encapsulación:
Crear clase de persona.
Cree las variables privadas edad, nombre y número de teléfono de la clase Persona.
Cree obtiene y conjuntos de cada propiedad.
Crea un objeto persona en main.
Utilice get y sets para dar valores a las propiedades de edad, nombre y teléfono. 
Finalmente, muéstralos a través de la consola.
"""

class Person:  
    def __init__(self,age,name,phone):
        self.age = age
        self.name = name
        self.phone = phone
        
    def set_age(self,age):
        self.age = age
    
    def set_name(self,name):
        self.name = name
    
    def set_phone(self,phone):
        self.phone = phone
    
    def get_age(self):
        return self.age

    def get_name(self):
        return self.name
    
    def get_phone(self):
        return self.phone

user = Person(age=29, name = "David", phone = "+57 123456789")

print("Nombre:",user.get_name())
print("Edad:",user.get_age(),"años")
print("Telefono:",user.get_phone())