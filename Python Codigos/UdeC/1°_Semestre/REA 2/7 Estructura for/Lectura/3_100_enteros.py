# Suma los primeros 100 numeros enteros

"""
Elabora un algoritmo que calcule e imprima la suma de los numeros enteros del 1 al 100
Analisis del problema:
1+2+3+4+5+....100=?

1+2+3+4+5+.....100 = n(n+1)/2  (Serie de Gauss)

si n = 2

2(2+1)/2 = 3

Si n=4

4(4+1)/2 = 10
"""
for i in range (101):
    suma = i * (i + 1)/ 2
print(f"{suma:.0f}")