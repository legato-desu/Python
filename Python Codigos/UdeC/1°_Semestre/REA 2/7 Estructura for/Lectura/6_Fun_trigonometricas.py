# Tabla de funciones trigonometricas 

import math
"""
Elaborar un algoritmo que imprima el valor del seno, coseno y arcotangente de X; para valores de 
X desde -1 hasta 1 con intervalos de 0.2. Debe imprimir la siguiente tabla.
    X       SENOX       COSENOX       ARCOTANGENTEX
    
    _______________________________________________
    
    -1.0    99.99        99.99           99.99
    -0.8    99.99        99.99           99.99
    .
    .
    .
    1.0     99.99        99.99           99.99
"""
def Tabla():
    print("X\t\tSENOX\t\tCOSENOX\t\tARCOTANGENTEX")
    print("-" * 60)
    for x in [i * 0.2 for i in range(-5, 6)]:
        senx = math.sin(x)
        cosx = math.cos(x)
        arcotangentex = math.atan(x)
        print(f"{x:.1f}\t\t{senx:.1f}\t\t{cosx:.1f}\t\t{arcotangentex:.1f}")
Tabla()