# Prime numbers
"""
Write a program that prints all prime numbers 
up to a number entered by the user.
"""
limit = int(input("Ingrese un mumero: "))
for number in range(1, limit + 1):
    possible_cousin = True
    for divider in range(2,number):
        if number % divider == 0:
            possible_cousin = False
            break
    if possible_cousin:
            print(number)