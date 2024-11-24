# Add three numbers
"""
Create a function with three parameters that are 
numbers that add to each other.
"""
print("\nSuma tres números")
print("=================\n")
def add (x, y, z):  
    return x + y + z
x = int(input("Primer numero: "))
y = int(input("Segundo numero: "))
z = int(input("Tercer numero: "))
print(f"{x} + {y} + {z} = {add(x,y,z)}")