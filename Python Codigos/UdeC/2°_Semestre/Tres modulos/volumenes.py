import math

def circunferencia(radio):
    """
    Calcula la longitud de la circunferencia de un círculo.

    Parámetros:
    radio (float): El radio del círculo.

    Retorna:
    float: La longitud de la circunferencia.
    """
    return 2 * math.pi * radio


def cono(radio, h):
    """
    Calcula el volumen de un cono.

    Parámetros:
    radio (float): El radio de la base del cono.
    h (float): La altura del cono.

    Retorna:
    float: El volumen del cono.
    """
    return (1/3) * math.pi * radio**2 * h


def cilindro(radio, h):
    """
    Calcula el volumen de un cilindro.

    Parámetros:
    radio (float): El radio de la base del cilindro.
    h (float): La altura del cilindro.

    Retorna:
    float: El volumen del cilindro.
    """
    return math.pi * radio ** 2 * h