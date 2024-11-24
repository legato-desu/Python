# Power table
"""
Create a code that powers a base number from 0 to 10 and
shows the result of each power
"""
print("\nTabla de potencia")
print("=================\n")
base = int(input("Introduce el numero a elevar: "))
for exponent in range(0,10):
    power = base ** exponent
    print(f"{base}^{exponent} = {power}")