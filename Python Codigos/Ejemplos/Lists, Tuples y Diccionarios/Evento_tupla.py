# Evento en Tuple

"""
Mostrar la fecha de un evento almacenado en una tupla
"""

event_date = (2024, 7, 26)
print(type(event_date))

print(f"El evento programado sera para la fecha {event_date}")
print("El evento programado sera para la fecha:",event_date)
print("El evento programado sera para la fecha: %i/%i/%i" % event_date)

year, month, day = event_date

print("El evento programado sera para la fecha {}/{}/{}".format(day, month, year))