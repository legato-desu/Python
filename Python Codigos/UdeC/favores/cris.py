import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Generar Contraseñas")
root.geometry("300x250")

# Opciones para el primer menú desplegable
opciones_menu1 = ["Facil", "Medio", "Dificil"]

# Opciones para el segundo menú desplegable
opciones_menu2 = ["Pregunta 1", "Pregunta 2", "Pregunta 3", "Etc"]

# Variable para almacenar las selecciones
seleccion_menu1 = tk.StringVar()
seleccion_menu2 = tk.StringVar()

# Función a ejecutar al presionar el botón "Generar"
def generar():
    print("Dificultad:", seleccion_menu1.get())
    print("Pregunta:", seleccion_menu2.get())
    print("Texto ingresado:", entrada_texto.get())

# Crear el primer menú desplegable
label_menu1 = tk.Label(root, text="Seleccione Dificultad:")
label_menu1.pack(pady=5)

menu1 = ttk.Combobox(root, textvariable=seleccion_menu1)
menu1['values'] = opciones_menu1
menu1.pack(pady=5)

# Crear el segundo menú desplegable
label_menu2 = tk.Label(root, text="Elija una pregunta:")
label_menu2.pack(pady=5)

menu2 = ttk.Combobox(root, textvariable=seleccion_menu2)
menu2['values'] = opciones_menu2
menu2.pack(pady=5)

# Crear el campo de entrada de texto
label_texto = tk.Label(root, text="Ingrese respuesta:")
label_texto.pack(pady=5)

entrada_texto = tk.Entry(root)
entrada_texto.pack(pady=5)

# Crear el botón "Generar"
boton_generar = tk.Button(root, text="Generar", command=generar)
boton_generar.pack(pady=10)

# Iniciar el bucle de la interfaz gráfica
root.mainloop()