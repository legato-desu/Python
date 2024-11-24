# Bandera Colombiana

import tkinter
"""
Crea una ventana con los colores de Colombia y su significado.
"""

window = tkinter.Tk()

label1 = tkinter.Label(window, text="Riquesa", bg="yellow", fg="black")
label1.pack(ipadx=50, ipady=50, fill="both")

label2 = tkinter.Label(window, text="Abundancia", bg="blue", fg="black")
label2.pack(ipadx=50, ipady=50, fill="both")

label3 = tkinter.Label(window, text="Sangre derramada ", bg="red", fg="black")
label3.pack(ipadx=50, ipady=50, fill="both")

window.mainloop()