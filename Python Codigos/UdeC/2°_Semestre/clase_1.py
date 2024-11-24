
salario = int(input("Ingrese salario: "))
horas_trabajadas = float(input("Horas trabajadas: "))
valor_final = salario / 30 /8 * horas_trabajadas

pendientes = int(input("Tareas pendientes: "))
proceso = int(input("Tareas en proceso: "))
hechas = int(input("Tareas hechas: "))
devueltas = int(input("Devueltas: "))

total_tareas = pendientes + proceso + hechas

valor_pendientes = (valor_final * 0.05) * pendientes
valor_proceso = (valor_final * 0.03) * proceso
valor_hechas = (valor_final * 0.08) * hechas
valor_devueltas = (valor_final * 0.1) * devueltas


rendimiento = ((hechas - devueltas )/ total_tareas) * 100

bonificacion = (valor_final * 0.08) * hechas
valor_total = valor_pendientes + valor_proceso + valor_devueltas

valor_pagar = bonificacion  + valor_final - valor_total
"""
print(f"\nDescuento pendientes: ${valor_pendientes:,.0f}")
print(f"Descuento Procesos: ${valor_proceso:,.0f}")
print(f"Descuento Devueltas: ${valor_devueltas:,.0f}")
"""
print(f"\nTuvo un rendimiento de: {rendimiento:.0f}%")
print(f"Bonificacion: ${bonificacion:,.0f}")
print(f"Valor descuento: ${valor_total:,.0f}")
print(f"\nSalario a pagar: ${valor_pagar:,.0f}")

if rendimiento > 90:
    print("Rendimiento excelente")
elif rendimiento >70 and rendimiento <=90:
    print("Rendimiento regular")
else:
    print("Rendimiento bajo")

