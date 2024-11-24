# Calcula valor ecuacion z

import math
from math import pi, sqrt
"""
Elaborar un  algoritmo que lea el valor de W e imprima el valor de Z, de la siguiente ecuación 

z = e**w**3  + Ln |w|
    √2 pi w  
"""
print('Z=  e**w**3  + Ln |w|\n\
    √2 pi w  ')

w = int(input('Ingresa el valor de W (con W > 0 ): '))

if w > 0:
    
    a = w**3        # w**3
    b = math.exp(a) # e**w**3
    c = 2*pi*w      # 2*pi*w
    d = sqrt(c)     # Raiz 2*pi*w
    f = abs(w)      # |w|
    g = math.log(f) # ln |w|
    z = b/d + g     # e**w**3 / Raiz 2*pi*w + ln |w|
    
    print(f"El valor de Z es: {z:,.2f}")
    
else:
    print('W debe ser entero positivo')