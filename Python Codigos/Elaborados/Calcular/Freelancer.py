# Calculadora Freelancer

"""
Un Freelancer quiere saber cuánto puede cobrar por su trabajo 
semanal y mensual, para esto solo necesitas establecer el 
Precio de tu trabajo por hora.

Se estima unas 40 horas de trabajo semanales.
Las Fórmulas para calcular el pago Semanal y Mensual son:

1) pago_semanal = (DólaresPorHora x 40)
2) pago_mensual = (Dólares Por Hora x 160)

►Variables:

Dollars_Per_Hour: Cantidad de dólares ganados por 
Freelancer por hora.

pago_semanal: almacena el resultado del pago semanal.
pago_mensual: Almacena el resultado del pago mensual.

► Salida:

----------------------------------------
    CALCULADORA FREELANCER (USD)      
----------------------------------------
>>> Precio en dolares por Hora: 20
----------------------------------------
>>> PAGO SEMANAL: 800.00
>>> PAGO MENSUAL: 3200.00
----------------------------------------
"""
broad = 40
filling_1 = "-"
filling_2 = " "
empty_string = ""
weekly_hours = 40
monthly_hours = 160
initial_message = "Calculadora Freelancer (USD)"
request_price = ">>> Precio en dolares por Hora: "
format_error = "Solo se permiten numeros"
weekly_payment, monthly_payment , dollars_per_hour,  = 0.0 , 0.0, 0.0
response_format = ">>> Pago Semanal: %4.2f\n>>> Pago Mensual: %4.2f"
print(empty_string.center(broad,filling_1))
print(initial_message.center(broad,filling_2))
print(empty_string.center(broad,filling_1))

try:
    dollars_per_hour   = float(input(request_price))
    weekly_payment = dollars_per_hour * weekly_hours
    monthly_payment = dollars_per_hour * monthly_hours
    print(empty_string.center(broad,filling_1))
    print(response_format %(weekly_payment,monthly_payment))
except ValueError:
    print(empty_string.center(broad,filling_1))
    print(format_error.center(broad,filling_2))

print(empty_string.center(broad,filling_1))