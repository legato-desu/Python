# Reverse order
"""
Create a program that prints the inverse word on the screen according to 
the one stored in the variable (string)
"""
chain = 'Python'
for i in range(len(chain)-1,-1,-1):
    print(chain[i],end='')