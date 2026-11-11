import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()

ventana.wm_title('Mi Primer Ventana 🤪')
ventana.wm_minsize(300,300)

etiqueta = tk.Label(ventana, text='Soy una etiqueta XD')
etiqueta.pack()

boton = tk.Button(ventana, text='Pushame 😈')
boton.pack()

ardilla = ImageTk.PhotoImage(Image.open('proyectada.jpeg'))

imagen = tk.Label(ventana, image=ardilla)
imagen.pack()

ventana.mainloop()