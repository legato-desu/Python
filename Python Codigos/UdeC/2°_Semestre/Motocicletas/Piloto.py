# Definimos la clase Piloto
class Piloto:
    # Inicializador de la clase Piloto
    def __init__(self, edad, categoria, peso):
        self.edad = edad  # Edad del piloto
        self.categoria = categoria  # Categoría en la que compite o a la que pertenece el piloto (por ejemplo, Moto GP, Motero, Turismo)
        self.peso = peso  # Peso del piloto en kilogramos (kg)
        
    # Método para mostrar los atributos del piloto
    def ver_atributos(self):
        print("\n  \___Piloto___/")  # Encabezado para la sección de atributos
        print("\t 😎")  # Icono que representa un piloto
        print(f" - Edad: {self.edad} años")  # Muestra la edad del piloto
        print(f" - Categoria: {self.categoria}")  # Muestra la categoría del piloto
        print(f" - Peso: {self.peso} kg")  # Muestra el peso del piloto en kg

# Crear instancias de la clase Piloto con diferentes edades, categorías y pesos
piloto_1 = Piloto(25, "Moto GP", 65)
piloto_2 = Piloto(19, "Motero", 57)
piloto_3 = Piloto(45, "Turismo", 76)

# Mostrar los atributos de cada piloto
piloto_1.ver_atributos()
piloto_2.ver_atributos()
piloto_3.ver_atributos()