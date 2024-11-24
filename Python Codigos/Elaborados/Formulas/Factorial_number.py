# Factorial number
"""
Write an algorithm to calculate the factorial of a number. 
Remember that the factorial of a number n is the product of all the numbers
positive integers from 1 to n
"""
print("\nNumero factorial")
print("=======\n")
number = int(input("Ingrese el numero para calcular su factorial: "))
def factorial(number):
    if (number ==0):
        return 1
    else:
        return number * factorial(number-1)
print(f"{number}! = {factorial(number)}")