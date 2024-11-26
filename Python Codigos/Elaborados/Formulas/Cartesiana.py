# Distancia carteciana

from math import sqrt
"""
Crear un programa para calcular la distancia entre dos puntos cartesianos
PI(x1, y1), P2(x2, y2)
"""

class spot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def calculate_distance(p1, p2):
    return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

spot1 = spot(3, 2)
spot2 = spot(-3, -5)
print(calculate_distance(spot1, spot2))