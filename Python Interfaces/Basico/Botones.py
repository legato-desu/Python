# Botones

import tkinter
"""
Crear una ventana para mostrar botones
"""

window = tkinter.Tk()
def greet(event):
    print("Han dado clic aqui")
def greetDobleClic(event):
    print("has dado doble clic")
def exit(event):
    window.quit()

boton = tkinter.Button(window, text="Clic aqui")
boton.pack()
boton.bind("<Button-1>",greet)
boton.bind("<Double-1>",greetDobleClic)

botonexit = tkinter.Button(window, text="Salir")
botonexit.pack()
botonexit.bind("<Button-1>",exit)
window.quit()

window.mainloop()