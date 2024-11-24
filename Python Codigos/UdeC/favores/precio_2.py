from datetime import datetime

def formato_reloj_precio_del_mañana(años, meses, dias, horas, minutos, segundos):
    # Ajuste de segundos a minutos
    minutos += segundos // 60
    segundos = segundos % 60

    # Ajuste de minutos a horas
    horas += minutos // 60
    minutos = minutos % 60

    # Ajuste de horas a días
    dias += horas // 24
    horas = horas % 24

    # Ajuste de días a meses (asumiendo un mes promedio de 30 días)
    meses += dias // 30
    dias = dias % 30

    # Ajuste de meses a años
    años += meses // 12
    meses = meses % 12

    # Aseguramos que cada valor tenga el número adecuado de dígitos usando zfill
    años_formato = str(años).zfill(4)
    meses_formato = str(meses).zfill(2)
    dias_formato = str(dias).zfill(2)
    horas_formato = str(horas).zfill(2)
    minutos_formato = str(minutos).zfill(2)
    segundos_formato = str(segundos).zfill(2)
    
    # Concatenamos los valores con el formato deseado
    tiempo_formateado = f"{años_formato}-{meses_formato}-{dias_formato}-{horas_formato}-{minutos_formato}-{segundos_formato}"
    
    return tiempo_formateado

def calcular_diferencia_entre_fechas(fecha_inicial, fecha_final):
    # Calcular la diferencia en segundos entre las dos fechas
    diferencia = fecha_final - fecha_inicial
    total_segundos = int(diferencia.total_seconds())
    
    # Convertimos los segundos a años, meses, días, horas, minutos y segundos
    años = total_segundos // (365 * 24 * 3600)
    total_segundos %= 365 * 24 * 3600

    meses = total_segundos // (30 * 24 * 3600)
    total_segundos %= 30 * 24 * 3600

    dias = total_segundos // (24 * 3600)
    total_segundos %= 24 * 3600

    horas = total_segundos // 3600
    total_segundos %= 3600

    minutos = total_segundos // 60
    segundos = total_segundos % 60

    return formato_reloj_precio_del_mañana(años, meses, dias, horas, minutos, segundos)

# Menú de opciones
print("Seleccione una opción:")
print("1. Ingresar años, meses, días, horas, minutos y segundos manualmente")
print("2. Ingresar fecha inicial y fecha final")

opcion = input("Opción (1 o 2): ")

if opcion == '1':
    # Solicitar datos al usuario
    años = int(input("Introduce los años: "))
    meses = int(input("Introduce los meses: "))
    dias = int(input("Introduce los días: "))
    horas = int(input("Introduce las horas: "))
    minutos = int(input("Introduce los minutos: "))
    segundos = int(input("Introduce los segundos: "))

    # Llamar a la función y mostrar el resultado
    resultado = formato_reloj_precio_del_mañana(años, meses, dias, horas, minutos, segundos)
    print("Tiempo en formato de 'El precio del mañana':", resultado)

elif opcion == '2':
    # Solicitar fecha inicial y final al usuario
    print("Introduce la fecha inicial (en formato 'AAAA-MM-DD HH:MM:SS'):")
    fecha_inicial = input("Fecha inicial: ")
    print("Introduce la fecha final (en formato 'AAAA-MM-DD HH:MM:SS'):")
    fecha_final = input("Fecha final: ")

    # Convertir las fechas a objetos datetime
    fecha_inicial = datetime.strptime(fecha_inicial, "%Y-%m-%d %H:%M:%S")
    fecha_final = datetime.strptime(fecha_final, "%Y-%m-%d %H:%M:%S")

    # Calcular la diferencia y mostrar el resultado
    resultado = calcular_diferencia_entre_fechas(fecha_inicial, fecha_final)
    print("Diferencia en formato de 'El precio del mañana':", resultado)

else:
    print("Opción no válida.")