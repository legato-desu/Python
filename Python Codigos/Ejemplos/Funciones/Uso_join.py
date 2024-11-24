# Ejecutar join

"""
Cree un programa para emular la operación de unión para concatenar una lista
número = [2, 3, 5, 7, 11]
# 2 3 5 7 11
print(''.join([str(n)para n en número]))
"""

def concatenate_list(list):
    result = ''
    for n in list:
        result += str(n)
    return result
numbers = [2, 3, 5, 7, 11]
print(concatenate_list(numbers))