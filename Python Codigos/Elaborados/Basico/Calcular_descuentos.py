# Calcular descuento

"""
En una fábrica de computadoras, se planea ofrecer a los clientes un descuento que dependerá del 
número de ordenadores que compres. Si los ordenadores son menos de cinco, se les hará un 10% de descuento. 
descuento sobre el total de ordenadores; Si el número de  computadoras es mayor o igual a cinco pero menor que diez 
Recibirás un 20% de descuento; y si son 10 o más se les da el 40% apagado. El precio de cada computadora es de $700.
"""

computers = int(input("Cantidad de computadoras compradas: "))
total = computers * 700

if computers < 5:
    total = total - (total * 0.10)

elif computers >= 5 and computers < 10:
    total = total - (total * 0.20)

elif computers >= 10:
    total = total - (total * 0.40)     

print(f"El total es de: ${total:,.0f}")