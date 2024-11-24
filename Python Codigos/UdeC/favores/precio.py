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