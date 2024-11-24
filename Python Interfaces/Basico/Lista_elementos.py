# Elementos de una lista

from tkinter import *
"""
Crear una interfaz simple que debe contener una lista de elementos seleccionables, también debe tener una etiqueta 
con el texto que desees.
"""

master = Tk()
master.title("Marcas")
master.geometry("200x210")
elemento = StringVar()
listbox = Listbox(master)

for item in ["Yamaha", "Suzuki", "kawasaki", "Honda"]:
    listbox.insert(END, item)

listbox.pack()
label = Label(text="Marcas de Motocicletas")
label.pack()
master.mainloop()