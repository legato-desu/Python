# Suma de n + nn + nnnn ...

"""
pedir al usuario un número n y calcular n + nn + nnn El código utilizará el número ingresado por el 
usuario y lo conectará con el mismo +1 para agregar ejemplo:

n = 2
2 + 22 + 222
>>> 246
"""

n = input("Ingrese el valor de n: ")
nn = int('{}{}'.format(n,n))
nnn = int('%s%s%s'%(n,n,n))
n = int(n)
sum = n + nn + nnn
print(sum)