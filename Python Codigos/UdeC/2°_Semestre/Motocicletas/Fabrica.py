# Definimos la clase Fabrica
class Fabrica:
    # Inicializador de la clase Fabrica
    def __init__(self, empresa, ubicacion, precio):
        self.empresa = empresa  # Nombre de la empresa que posee la fábrica
        self.ubicacion = ubicacion  # Ubicación de la fábrica
        self.precio = precio  # Precio de la fábrica en dólares
        
    # Método para mostrar los atributos de la fábrica
    def ver_atributos(self):
        print("\n \___Fabrica___/")  # Encabezado para la sección de atributos
        print("\t 🏭")  # Icono que representa una fábrica
        print(f" - Fabrica: {self.empresa}")  # Muestra el nombre de la empresa
        print(f" - Ubicacion: {self.ubicacion}")  # Muestra la ubicación de la fábrica
        # Muestra el precio de la fábrica con formato de miles
        print(f" - Precio: ${self.precio:,}")

# Crear instancias de la clase Fabrica con diferentes empresas y precios
fabrica_1 = Fabrica("Yamaha ", "Shizuoka", 120000000)
fabrica_2 = Fabrica("Suzuki", "Iwata-shi", 12999000)
fabrica_3 = Fabrica("Kawasaki", "Kobe", 79000000)

# Mostrar los atributos de cada fábrica
fabrica_1.ver_atributos()
fabrica_2.ver_atributos()
fabrica_3.ver_atributos()