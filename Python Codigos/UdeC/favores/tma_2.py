import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Generar Contraseña")
root.geometry("320x200") 

opcion_dificultad = ["Facil", "Medio", "Dificil"]
opcion_pregunta = ["Pregunta A", "Pregunta B", "Pregunta C", "Etc ......"]

elegir_dificultad = tk.StringVar()
elegir_pregunta = tk.StringVar()

def generar():
    print("Dificultad: ", elegir_dificultad.get())
    print("Pregunta: ", elegir_pregunta.get())
    print("Texto ingresado:", entrada_respuesta.get())

texto_dificultad = tk.Label(root, text="Elija Dificultad")
texto_dificultad.place(x=20, y=20)
texto_1 = ttk.Combobox(root, textvariable=elegir_dificultad)
texto_1['values'] = opcion_dificultad
texto_1.place(x=150, y=20)

texto_pregunta = tk.Label(root, text="Elija pregunta")
texto_pregunta.place(x=20, y=60)
texto_2 = ttk.Combobox(root, textvariable=elegir_pregunta)
texto_2['values'] = opcion_pregunta
texto_2.place(x=150, y=60)

texto_respuesta = tk.Label(root, text="Respuesta")
texto_respuesta.place(x=20, y=100)
entrada_respuesta = tk.Entry(root)
entrada_respuesta.place(x=150, y=100)

boton_generar = tk.Button(root, text="Generar", command=generar)
boton_generar.place(x=140, y=150)

root.mainloop()