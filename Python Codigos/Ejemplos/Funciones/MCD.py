# máximo común divisor

"""
Crea un programa para calcular el máximo común divisor de dos números.
"""

def mcd(x, y):
    mcd = 1
    if x % y == 0:
        return y
    for k in range(int(y/2),0,-1):
        if x % k == 0 and y % k == 0:
            mcd = k
            break
    return mcd

x = int(input("Ingrese el primer numero: "))
y = int(input("Ingrese el segundo numero: "))
print(f"El maximo comun divisor de {x} y {y} es: {mcd(x,y)}")