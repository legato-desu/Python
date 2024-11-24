# Definimos la clase Moto
class Moto:
    # Inicializador de la clase Moto
    def __init__(self, modelo, uso, cilindrada):
        self.modelo = modelo  # Nombre del modelo de la motocicleta
        self.uso = uso  # Tipo de uso que se le da a la motocicleta (por ejemplo, Carreras, Urbano, Touring)
        self.cilindrada = cilindrada  # Cilindrada de la motocicleta en centímetros cúbicos (cm³)
        
    # Método para mostrar los atributos de la motocicleta
    def ver_atributos(self):
        print("\n \___Motocicleta___/")  # Encabezado para la sección de atributos
        print("\t 🏍️")  # Icono que representa una motocicleta
        print(f" - Modelo: {self.modelo}")  # Muestra el modelo de la motocicleta
        print(f" - Uso: {self.uso}")  # Muestra el tipo de uso de la motocicleta
        # Muestra la cilindrada de la motocicleta con formato de miles seguido de 'cm³'
        print(f" - Cilindrada: {self.cilindrada:,}cm³")

# Crear instancias de la clase Moto con diferentes modelos, usos y cilindradas
moto_1 = Moto("YZF-R1M", "Carreras", 998)
moto_2 = Moto("Gixxer", "Urbano", 250)
moto_3 = Moto("GTR", "Touring", 1352)

# Mostrar los atributos de cada motocicleta
moto_1.ver_atributos()
moto_2.ver_atributos()
moto_3.ver_atributos()