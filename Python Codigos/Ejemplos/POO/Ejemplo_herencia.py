# Inheritance example

"""
Cree una jerarquía de herencia básica.
Persona <- Estudiante
"""

class Person:
    def __init__(self, document, name, mail):
        self.document = document
        self.name = name
        self.mail = mail

class Student(Person):
    def __init__(self, document, name, mail, license, career):
        super().__init__(document, name, mail)        
        self.license = license
        self.career = career

david = Student("950625","David","Prueba-python@col.co","15143","Programador") 

print(isinstance(david, Student))
print(isinstance(david, Person))