# Números impares

from functools import reduce
"""
crear una aplicación que obtenga los elementos impares de un lista pasada por parámetro con (filtro) y 
realizará una suma de todos estos elementos obtenidos a través de (reducir).
"""

def addition(numbers): 
    result = list(filter((lambda x: x % 2), numbers)) 
    print(result)
    result = reduce( (lambda x, y: x + y), result) 
    print(result)
    
numbers = list(range(50))

addition(numbers)