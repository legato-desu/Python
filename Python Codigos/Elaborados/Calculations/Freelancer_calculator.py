# Freelancer calculator
"""
A Freelancer wants to know how much he can charge for his work 
weekly and monthly, for this you only need to establish the 
price of your work per hour.

An estimated 40 hours of work per week.
The Formulas to calculate the Weekly and Monthly payment are:

1) weekly_payment = (DollarsPerHour x 40)
2) monthly_payment = (DollarsPerHour x 160)

► Variables:

Dollars_Per_Hour: Amount of Dollars earned by 
Freelancer per hour.

weekly_payment: Stores the weekly payment result.
monthly_payment: Stores the result of the monthly payment.

► Output:

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