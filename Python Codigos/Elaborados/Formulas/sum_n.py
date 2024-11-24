# sum of n + nn + nnnn ...
"""
ask the user for a number n and calculate n + nn + nnn
The code will use the number entered by the user and connect it 
with the same +1 to add
example:
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