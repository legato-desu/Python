# Inicio

import tkinter
from tkinter import ttk
"""
Crear una ventana de inicio de sesión de usuario
"""

window = tkinter.Tk()

window.title("Legato")
window.geometry("230x110")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

username_label = ttk.Label(window, text="Usuario:")
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

username_entry = ttk.Entry(window)
username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

password_label = ttk.Label(window, text="Contraseña:")
password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

password_entry = ttk.Entry(window, show="*")
password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

login_button = ttk.Button(window, text="Ingreso")
login_button.grid(column=1, row=3, sticky=tkinter.E, padx=5, pady=5)

window.mainloop()