# Calculate discount
"""
In a computer factory, it is planned to offer customers 
a discount that will depend on the number of computers you buy. 
If the computers are less than five, they will be given a 10% discount. 
discount on the total of computers; If the number of 
computers is greater than or equal to five but less than ten 
You will be given a 20% discount; and if there are 10 or more they are given 40% 
off. The price of each computer is $700.
"""
print("\nCalcular descuento")
print("==================\n")
computers = int(input("Cantidad de computadoras compradas: "))
total = computers * 700    
if computers < 5:
    total = total - (total * 0.10)
elif computers >= 5 and computers < 10:
    total = total - (total * 0.20)
elif computers >= 10:
    total = total - (total * 0.40)     
print(f"El total es de: ${total:,.0f}")