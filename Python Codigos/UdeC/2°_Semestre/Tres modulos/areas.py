# Importamos el módulo math para operaciones matemáticas y el módulo principal que contiene la función principal()
import math, principal

# Definimos una función que calcula el área de un círculo
def circulo(radio):
    # Devuelve el área de un círculo utilizando la fórmula π * radio^2
    return math.pi * radio ** 2

# Definimos una función que calcula el área de un triángulo
def triangulo(a, h):
    # Devuelve el área de un triángulo utilizando la fórmula (base * altura) / 2
    return (a * h) / 2

# Definimos una función que calcula el área de un rombo
def rombo(mayor, menor):
    # Devuelve el área de un rombo utilizando la fórmula (diagonal mayor * diagonal menor) / 2
    return (mayor * menor) / 2

# Este bloque asegura que el código dentro de la condición __name__ == "__main__" solo se ejecute si este archivo
# es ejecutado directamente, y no cuando es importado como módulo.
if __name__ == "__main__":
    # Llama a la función principal() definida en el archivo principal.py, que se supone que imprime un mensaje.
    principal.principal()

"""
Al ejecutar este código "areas.py", que tiene una importación de "principal.py", se lanzará por pantalla
el mensaje contenido en el módulo "principal.py". Este mensaje simula la ejecución de un ejemplo de módulos,
mostrando "Ejemplo de modulos".
"""
