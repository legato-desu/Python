# Lista seleccion

from tkinter import *
"""
Cree una lista de botones de radio que muestre la opción que se ha seleccionado y contenga 
un botón de reset para dejar todo como estaba al principio.

Al principio no es necesario que haya una opción seleccionada.
"""
def select():
    monitor.config(text="{}".format(opcion.get()))
def reset():
    opcion.set(None)
    monitor.config(text="")

root = Tk()
opcion = StringVar()
opcion.set(None)
root.title("Legato")

Radiobutton(root, text="Anime", variable=opcion, value="Anime", command=select).pack(anchor=W)
Radiobutton(root, text="Cosplay", variable=opcion, value="Cosplay", command=select).pack(anchor=W)
Radiobutton(root, text="Manga", variable=opcion, value="Manga", command=select).pack(anchor=W)
Radiobutton(root, text="Japon", variable=opcion, value="Japon", command=select).pack(anchor=W)

monitor = Label(root)
monitor.pack()
Button(root, text="Limpiar", command=reset, fg="blue").pack()

root.mainloop()