"""
La empresa le asigna para cada periodo a los programadores una cantidad de tareas:
Pendientes (-5%), En Proceso (-3%), Hechas (+8%), Devueltas (-10%).
Calcule el rendimiento en porcentaje del trabajador de acuerdo a:


                Tareas hechas - Tareas devueltas
                        Tareas totales

imprima el Vr. Bonificaciones el Vr. Descuentos y el Vr Pagar 

        ╔══════════════════════════════════════════════════════════════════╗
        ║      -5%     ║    -3%     ║    8%     ║    -10%    ║             ║
        ╠══════════════╣════════════╣═══════════╣════════════╣═════════════╣        
        ║  Pendientes  ║ En proceso ║  Hechas   ║ Devueltas  ║ Rendimiento ║
        ╠══════════════╣════════════╣═══════════╣════════════╣═════════════╣
        ║      4       ║      5     ║    11     ║      6     ║     25%     ║
        ║      1       ║      1     ║    18     ║      2     ║     80%     ║
        ║      3       ║      4     ║    13     ║      5     ║     40%     ║
        ╚══════════════════════════════════════════════════════════════════╝
"""
# Inicializamos la variable acumulada para el total de salarios.
acumulado = 0

# Solicitamos el número de empleados a registrar.
empleados = int(input("\n\tNo. empleados a registrar: "))

"""
Función que calcula la bonificación de un empleado Recibe el valor final del salario y la cantidad de tareas hechas.
Devuelve la bonificación calculada como el 8% del valor final multiplicado por las tareas hechas.
"""
def calcular_bonificacion(valor_final, hechas):
    return (valor_final * 0.08) * hechas

"""
Función que calcula los descuentos de un empleado Recibe el valor final del salario, la cantidad de tareas pendientes, 
en proceso y devueltas Devuelve el total de descuentos que se componen de un porcentaje de cada tipo de tarea.
"""
def calcular_descuentos(valor_final, pendientes, proceso, devueltas):
    valor_pendientes = (valor_final * 0.05) * pendientes
    valor_proceso = (valor_final * 0.03) * proceso
    valor_devueltas = (valor_final * 0.1) * devueltas
    return valor_pendientes + valor_proceso + valor_devueltas

# Bucle que se ejecuta por cada empleado registrado.
for i in range (empleados):
    print(f"\n\tIngrese el {i+1}° empleado:\n")
    
    salario = int(input(f"Empleado No.{i+1} salario: "))
    horas_trabajadas = float(input(f"Empleado No.{i+1} Horas trabajadas: "))
    
    # Calculamos el valor final del salario basado en las horas trabajadas.
    valor_final = salario / 30 / 8 * horas_trabajadas

    pendientes = int(input(f"Empleado No.{i+1} Tareas pendientes: "))
    proceso = int(input(f"Empleado No.{i+1} Tareas en proceso: "))
    hechas = int(input(f"Empleado No.{i+1} Tareas hechas: "))
    devueltas = int(input(f"Empleado No.{i+1} Devueltas: "))

    # Calculamos el total de tareas y el rendimiento del empleado.
    total_tareas = pendientes + proceso + hechas
    rendimiento = ((hechas - devueltas) / total_tareas) * 100

    # Llamamos a las funciones para calcular bonificación y descuentos
    bonificacion = calcular_bonificacion(valor_final, hechas)
    valor_total_descuentos = calcular_descuentos(valor_final, pendientes, proceso, devueltas)

    # Calculamos el salario total a pagar restando los descuentos y sumando la bonificación.
    valor_pagar = bonificacion + valor_final - valor_total_descuentos

    # Mostramos el rendimiento del empleado según el porcentaje calculado.
    if rendimiento > 90:
        print(f"\nRendimiento Empleado No.{i+1}: \t{rendimiento:.0f}%: EXCELENTE")
    elif rendimiento >70 and rendimiento <=90:
        print(f"\nRendimiento Empleado No.{i+1}: \t{rendimiento:.0f}%: REGULAR")
    else:
        print(f"\nRendimiento Empleado No.{i+1}: \t{rendimiento:.0f}%: BAJO")
    
    print(f"Empleado No.{i+1} Bonificación: \t${bonificacion:,.0f}")
    print(f"Empleado No.{i+1} Valor descuento: \t${valor_total_descuentos:,.0f}")
    print(f"\nEmpleado No.{i+1} Salario: \t\t${valor_pagar:,.0f}")

    # Acumulamos el valor a pagar en la variable acumulada de salarios.
    acumulado += valor_pagar

print(f"\n\tEl Salario acumulado: ${acumulado:,.0f}\n")

# Pausamos la ejecución del programa hasta que se presione una tecla.
input()