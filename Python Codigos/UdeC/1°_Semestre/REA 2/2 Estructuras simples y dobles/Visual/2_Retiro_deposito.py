# Transaccion

"""
Crea un programa que dado los siguientes datos de entrada: 
saldo anterior, tipo de movimiento R (retiro) o D (deposito) y monto de transaccion, 
obtener como dato la salida el saldo actual
"""
print("(D) Deposito\n(R) Retiro")

tipo_movimiento = input("Tipo de movimiento (D) o (R): ")
tipo_movimiento = tipo_movimiento.capitalize()
santerior = int(input("Ingrese el saldo anterior: "))

if tipo_movimiento == "D":
    monto_transaccion = int(input("ingrese el nuevo monto: "))
    sactual = santerior + monto_transaccion
    print(f"Saldo actual: ${sactual:,.0f}")
elif tipo_movimiento == "R":
    monto_transaccion = int(input("ingrese el nuevo monto: "))
    sactual = santerior - monto_transaccion
    print(f"Saldo actual: ${sactual:,}")
else:
    print("Movimiento no valido")