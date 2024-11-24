# Herencia

"""
Cree una clase Persona con las siguientes variables:

Edad
Nombre
el telefono

Una vez creada la clase, cree una nueva clase de Cliente que herede 
de Persona, esta nueva clase tendrá la variable crédito únicamente 
para esa clase.

Ahora crea un objeto de la clase Cliente que debe tener como 
propiedades, edad, número de teléfono, nombre y crédito, 
Hay que darles valor y mostrarlos en pantalla.

Una vez hecho esto, haga lo mismo con la clase Trabajador que 
hereda de Persona, y con una variable salario que solo tiene 
la clase trabajadora.
"""

class Person():
    def __init__(self,name,age,phone):
        self.name = name
        self.age = age
        self.phone = phone 
    
    def user(self):
        print("Nombre:", self.name, "Edad:", self.age, "Telefono:", self.phone)    
    
class Client (Person):
    def __init__(self, name, age, phone,credit):
        super().__init__(name, age, phone)
        self.credit = credit
    
    def user(self):
        super().user()
        print("El credit fue", self.credit)
    
class Job (Person):
    def __init__(self, name, age, phone,salary):
        super().__init__(name, age, phone)
        self.salary = salary
    
    def user(self):
        super().user()
        print(f"El salario es: ${(self.salary):,.0f}")

Persona_1 = Client ("David","29","+571234567","Aprobado")
Persona_1.user()
Job_1 = Job("Jorge","27","+57290834",4086590)
Job_1.user()