import tkinter as tk
from PIL import Image, ImageTk
ventana = tk.Tk()
ventana.wm_title("Mi Primer Ventana 😈")
ventana.wm_minsize(600,600)
etiqueta = tk.Label(ventana, text="Soy una etiqueta")
etiqueta.pack()
boton = tk.Button(ventana, text="Clickeame 😉")
boton.pack()
gato = ImageTk.PhotoImage(Image.open("gato.jpeg"))
imagen = tk.Label(ventana, image=gato)
imagen.pack()
ventana.mainloop()