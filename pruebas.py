import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import messagebox
import pydicom
import cv2
from PIL import Image,ImageTk,ImageGrab

# Función a ejecutar al hacer clic en el botón
def implantes():
    def drag_start(event):
        widget = event.widget
        if widget == label:
            widget.startX = 0
            widget.startY = 0
        else: 
            widget.startX = event.x
            widget.startY = event.y

    def drag_motion(event):
        widget = event.widget
        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y
        widget.place(x=x,y=y)

    def seleccionImplantes(valor):
        global im2, label
        if valor=='DHS':
            im2 = Image.open('./Imagenes/dhs.png')
            im2.thumbnail((50,100))
            im2=ImageTk.PhotoImage(im2)
            label = ttk.Label(canvas, image=im2)
            label.place(x=50, y=50)
            label.bind("<Button-1>", drag_start)
            label.bind("<B1-Motion>", drag_motion)
        else:
            im2 = Image.open('./Imagenes/clavo.jpg')
            im2.thumbnail((50,100))
            im2=ImageTk.PhotoImage(im2)
            label = ttk.Label(canvas, image=im2)
            label.place(x=50, y=50)
            label.bind("<Button-1>", drag_start)
            label.bind("<B1-Motion>", drag_motion)

    nueva_ventana = tk.Toplevel(root)
    # Configura la nueva ventana
    nueva_ventana.title("Nueva Ventana")
    nueva_ventana.geometry("400x300")
    # Carga la imagen en la nueva ventana
    ttk.Label(nueva_ventana, image=implantes_tk).place(x = 0, y = 0, relheight = 1, relwidth = 1)
    botonDHS=ttk.Button(nueva_ventana,text='DHS',command=lambda:seleccionImplantes(botonDHS.cget('text')))
    botonDHS.place(x=200, y=70)
    botonClavo=ttk.Button(nueva_ventana,text='Clavo',command=lambda:seleccionImplantes(botonClavo.cget('text')))
    botonClavo.place(x=200,y=200)
    
    
# Crea una ventana de Tkinter
root = tk.Tk()

# Carga la imagen
imagen = Image.open("./Imagenes/ana pau.png")
implantes_img = Image.open("./Fondos/Implantes.png")
implantes_tk = ImageTk.PhotoImage(implantes_img)
# Crea un canvas para mostrar la imagen
canvas = tk.Canvas(root, width=imagen.width, height=imagen.height)
canvas.pack()

# Crea una instancia de ImageTk para mostrar la imagen en Tkinter
imagen_tk = ImageTk.PhotoImage(imagen)

# Muestra la imagen en el canvas
canvas.create_image(0, 0, anchor=tk.NW, image=imagen_tk)

# Crea un botón debajo de la imagen
boton = tk.Button(root, text="Implantes", command=implantes)
boton.pack()

# Ejecuta el bucle principal de Tkinter
root.mainloop()
