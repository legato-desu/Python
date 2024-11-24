# Odd numbers

from functools import reduce
"""
create an application that will get the odd elements from a 
list passed by parameter with (filter) and will perform a sum 
of all these elements obtained through (reduce).
"""
def addition(numbers): 
    result = list(filter((lambda x: x % 2), numbers)) 
    print(result)
    result = reduce( (lambda x, y: x + y), result) 
    print(result)
numbers = list(range(100))
addition(numbers)