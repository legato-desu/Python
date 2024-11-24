"""
Visualización de audio en tiempo real con colores dinámicos.
Este script captura audio en tiempo real desde el micrófono y muestra la forma de onda con 
colores que cambian aleatoriamente.
"""

import numpy as np
import pyaudio
import matplotlib.pyplot as plt 
import struct
import random

# Configuración de parámetros de audio
FORMAT = pyaudio.paInt16    # Formato de audio: 16 bits por muestra
CHANNELS = 1                # Número de canales de audio (1 = mono)
RATE = 44100                # Tasa de muestreo (frecuencia de muestreo en Hz)
CHUCK = 1024                # Número de frames por buffer (tamaño del chunk)

# Inicialización de PyAudio
p = pyaudio.PyAudio()

# Apertura del stream de audio para la captura en tiempo real
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,                 # Captura de audio desde el micrófono
                frames_per_buffer=CHUCK)    # Buffer del tamaño de "CHUCK"

# Configuración de la visualización de la forma de onda
fig, ax = plt.subplots()
x = np.arange(0, 2 * CHUCK, 2)                      # Eje x: valores desde 0 hasta 2 * CHUCK, con paso de 2
line, = ax.plot(x, np.random.rand(CHUCK), lw=3)     # Inicialización de la gráfica con datos aleatorios

# Límites del gráfico
ax.set_ylim(-2**15 * 1.5, 2**15 * 1.5)      # Ajuste del rango del eje y
ax.set_xlim(0, CHUCK)                       # Ajuste del rango del eje x

# Ajustes de estilo del gráfico
plt.axis('off')                             # Oculta los ejes
fig.patch.set_facecolor('black')            # Fondo negro para el gráfico
line.set_color('cyan')                      # Color inicial de la línea

# Habilitar modo interactivo para actualizar la visualización en tiempo real
plt.ion()
plt.show()

# Bucle principal para la captura y visualización de audio en tiempo real
try:
    while True:
        # Leer datos de audio desde el stream
        data = stream.read(CHUCK)

        # Convertir los datos binarios en una lista de enteros
        data_int = struct.unpack(str(CHUCK) + 'h', data)
        
        # Cambiar el color de la línea aleatoriamente entre cyan, magenta y amarillo
        line.set_color(random.choice(['cyan', 'magenta', 'yellow']))
        
        # Actualizar los datos de la línea para reflejar la forma de onda
        line.set_ydata(np.array(data_int) * 5)
        
        # Redibujar el gráfico para mostrar la actualización
        fig.canvas.draw()
        fig.canvas.flush_events()

# Manejo de la interrupción con Ctrl+C
except KeyboardInterrupt:
    print("Visualizacion terminada.")

# Cierre de los recursos al finalizar
finally:
    stream.stop_stream()        # Detener el stream de audio
    stream.close()              # Cerrar el stream
    p.terminate()               # Terminar la instancia de PyAudio
    plt.close(fig)              # Cerrar la ventana de la gráfica