import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import messagebox
import pydicom
import cv2
from PIL import Image,ImageTk

def clasificar():
    def ClasFinal(valor):
        print(valor)
        clasificacion.destroy()
    def regvent30():
        clasificacion.destroy()
        clasificar()
    def vent31 ():
        tk.Label(clasificacion, image=fondo31tk).place(x = 0, y = 0, relheight = 1, relwidth = 1)
        botonRegTro = tk.Button(clasificacion, text = 'Region Trocantérea', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2',  command= vent31A)
        botonCuello = tk.Button(clasificacion, text = 'Fractura de Cuello', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2', command = vent31B)
        botonCabeza = tk.Button(clasificacion, text = 'Fractura de Cabeza', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2',command=vent31C)
        botonRegresar = tk. Button (clasificacion, text = 'Regresar', font = ('Canva Sans', 17,'bold'),  fg='#ffffff', bg = '#4a4a4a', cursor='hand2', command=regvent30)
        botonRegresar.place(x=0,y=0)
        botonCabeza.place(x=228,y=530)
        botonCuello.place(x=230,y=325)
        botonRegTro.place(x=230,y=120)
    def vent31A ():
        tk.Label(clasificacion, image=fondo31Atk ).place(x = 0, y = 0, relheight = 1, relwidth = 1)
        botonA11 = tk.Button(clasificacion, text = '31A1.1', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(botonA11.cget('text')))
        botonA11.place(x=157+9,y=82+9)
        botonA12 = tk.Button(clasificacion, text = '31A1.2', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(botonA12.cget('text')))
        botonA12.place(x=157+9,y=230+9)
        botonA13 = tk.Button(clasificacion, text = '31A1.3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(botonA13.cget('text')))
        botonA13.place(x=157+9,y=381+9)
        botonA22 = tk.Button(clasificacion, text = '31A2.2', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg ='#000000', bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(botonA22.cget('text')))
        botonA22.place(x=157+9,y=527+9)
        botonA23 = tk.Button(clasificacion, text = '31A2.3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(botonA23.cget('text')))
        botonA23.place(x=330+166,y=82+10)
        botonA31 = tk.Button(clasificacion, text = '31A3.1', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(botonA31.cget('text')))
        botonA31.place(x=330+166,y=230+10)
        botonA32 = tk.Button(clasificacion, text = '31A3.2', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(botonA32.cget('text')))
        botonA32.place(x=330+166,y=381+10)
        botonA33 = tk.Button(clasificacion, text = '31A3.3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(botonA33.cget('text')))
        botonA33.place(x=330+166,y=527+10)
        botonRegresar = tk. Button (clasificacion, text = 'Regresar', font = ('Canva Sans', 17,'bold'),  fg='#ffffff', bg = '#4a4a4a', cursor='hand2', command= vent31)
        botonRegresar.place(x=0,y=0)
    def vent31B ():
        tk.Label(clasificacion, image=fondo31Btk ).place(x = 0, y = 0, relheight = 1, relwidth = 1)
        botonA11 = tk.Button(clasificacion, text = '31B1.1', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2')
        botonA11.place(x=157+9,y=82+9)
        botonA12 = tk.Button(clasificacion, text = '31B1.2', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2')
        botonA12.place(x=157+9,y=230+9)
        botonA13 = tk.Button(clasificacion, text = '31B1.3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2')
        botonA13.place(x=157+9,y=381+9)
        botonA22 = tk.Button(clasificacion, text = '31B2.1', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg ='#000000', bg ='#e1e1e1', cursor='hand2')
        botonA22.place(x=157+9,y=527+9)
        botonA23 = tk.Button(clasificacion, text = '31B2.2', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2')
        botonA23.place(x=330+166,y=82+10)
        botonA31 = tk.Button(clasificacion, text = '31B2.3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2')
        botonA31.place(x=330+166,y=230+10)
        botonA32 = tk.Button(clasificacion, text = '31B3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2')
        botonA32.place(x=330+166,y=381+10)
        botonRegresar = tk. Button (clasificacion, text = 'Regresar', font = ('Canva Sans', 17,'bold'),  fg='#ffffff', bg = '#4a4a4a', cursor='hand2', command=vent31)
        botonRegresar.place(x=0,y=0)   
    def vent31C ():
        tk.Label(clasificacion, image=fondo31Ctk ).place(x = 0, y = 0, relheight = 1, relwidth = 1)
        botonA11 = tk.Button(clasificacion, text = '31C1.1', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2')
        botonA11.place(x=157+9,y=82+9)
        botonA12 = tk.Button(clasificacion, text = '31C1.2', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2')
        botonA12.place(x=157+9,y=230+9)
        botonA13 = tk.Button(clasificacion, text = '31C1.3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2')
        botonA13.place(x=157+9,y=381+9)
        botonA22 = tk.Button(clasificacion, text = '31C2.1', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg ='#000000', bg ='#e1e1e1', cursor='hand2')
        botonA22.place(x=157+9,y=527+9)
        botonA23 = tk.Button(clasificacion, text = '31C2.2', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2')
        botonA23.place(x=330+166,y=82+10)
        botonA31 = tk.Button(clasificacion, text = '31C2.3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2')
        botonA31.place(x=330+166,y=230+10)
        botonRegresar = tk. Button (clasificacion, text = 'Regresar', font = ('Canva Sans', 17,'bold'),  fg='#ffffff', bg = '#4a4a4a', cursor='hand2', command=vent31)
        botonRegresar.place(x=0,y=0)   
    def vent32 ():
        tk.Label(clasificacion, image=fondo32tk).place(x = 0, y = 0, relheight = 1, relwidth = 1)
        botonSimple = tk.Button(clasificacion, text = 'Simple', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2',command=vent32A)
        botonCuna = tk.Button(clasificacion, text = 'Cuña', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2',command=vent32B)
        botonMultifrag = tk.Button(clasificacion, text = 'Multifragmentaria', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2',command=vent32C)
        botonSimple.place(x=295,y=122)
        botonCuna.place(x=302,y=330)
        botonMultifrag.place(x=240,y=530)
        botonRegresar = tk. Button (clasificacion, text = 'Regresar', font = ('Canva Sans', 17,'bold'),  fg='#ffffff', bg = '#4a4a4a', cursor='hand2', command=regvent30)
        botonRegresar.place(x=0,y=0)
    def vent32A ():
        tk.Label(clasificacion, image=fondo32Atk ).place(x = 0, y = 0, relheight = 1, relwidth = 1)
        botonSpiral = tk.Button(clasificacion, text = 'En espiral', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2')
        botonOblique = tk.Button(clasificacion, text = 'Oblicua (>30°)', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2')
        botonTransverse = tk.Button(clasificacion, text = 'Transversal (<30°)', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2')
        botonSpiral.place(x=280,y=122)
        botonOblique.place(x=260,y=330)
        botonTransverse.place(x=240,y=530)
        botonRegresar = tk. Button (clasificacion, text = 'Regresar', font = ('Canva Sans', 17,'bold'),  fg='#ffffff', bg = '#4a4a4a', cursor='hand2', command=vent32)
        botonRegresar.place(x=0,y=0)
    def vent32B ():
        tk.Label(clasificacion, image=fondo32Btk ).place(x = 0, y = 0, relheight = 1, relwidth = 1)
        botonIntact = tk.Button(clasificacion, text = ' Cuña intacta', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2')
        botonFragment = tk.Button(clasificacion, text = 'Cuña fragmentaria', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2')
        botonIntact.place(x=250,y=160)
        botonFragment.place(x=222,y=465)
        botonRegresar = tk. Button (clasificacion, text = 'Regresar', font = ('Canva Sans', 17,'bold'),  fg='#ffffff', bg = '#4a4a4a', cursor='hand2', command=vent32)
        botonRegresar.place(x=0,y=0)
    def vent32C ():
        tk.Label(clasificacion, image=fondo32Ctk ).place(x = 0, y = 0, relheight = 1, relwidth = 1)
        botonIntact = tk.Button(clasificacion, text = ' Segmentaria intacta', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2')
        botonFragment = tk.Button(clasificacion, text = 'Segmentaria fragmentaria', relief= 'flat', font=('Canva Sans', 17), bg ='#b2b2b2', cursor='hand2')
        botonIntact.place(x=215,y=160)
        botonFragment.place(x=184,y=465)
        botonRegresar = tk. Button (clasificacion, text = 'Regresar', font = ('Canva Sans', 17,'bold'),  fg='#ffffff', bg = '#4a4a4a', cursor='hand2', command=vent32)
        botonRegresar.place(x=0,y=0)

    clasificacion = tk.Toplevel()
    clasificacion.geometry('650x650')
    clasificacion.title('Clasificacion AO')
    clasificacion.iconbitmap("./hueso.ico")
    # Fondo clases 30's
    fondo30s = Image.open('./Fondos/ClasFemur.png')
    fondo30stk = ImageTk.PhotoImage(fondo30s)
    # Fondo clase 31
    fondo31 = Image.open('./Fondos/ClasCabeza.png')
    fondo31tk = ImageTk.PhotoImage(fondo31)
    # Fondo clase 31A
    fondo31A = Image.open('./Fondos/ClasSubCabeza.png')
    fondo31Atk = ImageTk.PhotoImage(fondo31A)
    # Fondo clase 31B
    fondo31B = Image.open('./Fondos/ClasSubCabeza31B.png')
    fondo31Btk = ImageTk.PhotoImage(fondo31B)
    # Fondo clase 31C
    fondo31C = Image.open('./Fondos/ClasSubCabeza31C.png')
    fondo31Ctk = ImageTk.PhotoImage(fondo31C)
    # Fondo clase 32
    fondo32 = Image.open('./Fondos/ClasDiafisis.png')
    fondo32tk = ImageTk.PhotoImage(fondo32)
    # Fondo clase 32
    fondo32A = Image.open('./Fondos/ClasSubDiaf32A.png')
    fondo32Atk = ImageTk.PhotoImage(fondo32A)
    # Fondo clase 32
    fondo32B = Image.open('./Fondos/ClasSubDiaf32B.png')
    fondo32Btk = ImageTk.PhotoImage(fondo32B)
    # Fondo clase 32
    fondo32C = Image.open('./Fondos/ClasSubDiaf32C.png')
    fondo32Ctk = ImageTk.PhotoImage(fondo32C)

    
    tk.Label(clasificacion, image=fondo30stk).place(x = 0, y = 0, relheight = 1, relwidth = 1)
    # Botones Clas30s
    botonSegProx = tk.Button(clasificacion, text = 'Segmento proximal',relief ='flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2', command= vent31)
    botonSegProx.place(x=240,y=122)
    botonDiaf = tk.Button(clasificacion, text = 'Diáfisis', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2',command=vent32)
    botonDiaf.place(x=310,y=325)
    botonSegDist = tk.Button(clasificacion, text = 'Segmento distal', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2')
    botonSegDist.place(x=260,y=540)

    clasificacion.mainloop()
def infoPaciente():
    global entryNombre, entryNombre2, entryFecha, entryFecha2, entryEdad, entryEdad2, ClicksNotas
    def TerminarPaciente():
        paciente.withdraw()
    paciente=tk.Toplevel()
    paciente.title('Información del Paciente')
    paciente.iconbitmap("./hueso.ico")
    #Etiquetas
    nombrePaciente=tk.Label(paciente,text='Nombre del Paciente:')
    nombrePaciente.grid(column=0,row=0,pady=(10,0))
    edadPaciente=tk.Label(paciente,text='Edad del Paciente:')
    edadPaciente.grid(column=0,row=1,pady=(10,0))
    fecha=tk.Label(paciente,text='Fecha:')
    fecha.grid(column=0,row=2)
    #Buton
    botonListo=tk.Button(paciente,text='Listo',command=TerminarPaciente)
    botonListo.grid(column=0,row=5, pady=(20,20),padx=(130,0))

    #if messagebox.askokcancel("Cerrar ventana", "¿Estás seguro de que quieres cerrar la ventana?"):
    def on_closing():
        paciente.withdraw()
    # Asignar la función al evento "WM_DELETE_WINDOW"
    paciente.protocol("WM_DELETE_WINDOW", on_closing)
    if ClicksNotas==0:
        entryNombre=tk.Entry(paciente)
        entryNombre.insert(0,entryNombre2.get())
        entryNombre.grid(column=1,row=0,pady=(10,0),padx=(0,10))
        entryEdad=tk.Entry(paciente)
        entryEdad.insert(0,entryEdad2.get())
        entryEdad.grid(column=1,row=1,pady=(10,0),padx=(0,10))
        entryFecha=tk.Entry(paciente)
        entryFecha.insert(0,entryFecha2.get())
        entryFecha.grid(column=1,row=2,pady=(10,0),padx=(0,10))
        ClicksNotas+=1
    else:
        entryNombre2 = tk.Entry(paciente)
        entryNombre2.insert(0,entryNombre.get())
        entryNombre2.grid(column=1,row=0,pady=(10,0),padx=(0,10))
        entryEdad2 = tk.Entry(paciente)
        entryEdad2.insert(0,entryEdad.get())
        entryEdad2.grid(column=1,row=1,pady=(10,0),padx=(0,10))
        entryFecha2=tk.Entry(paciente)
        entryFecha2.insert(0,entryFecha.get())
        entryFecha2.grid(column=1,row=2,pady=(10,0),padx=(0,10))
        ClicksNotas=0
def herramientas():
    global Clicks
    #Botones Herramientas
    if Clicks==0:
        botonPaciente.grid(column=0, row = 2, padx=10)
        botonSelec.grid(column=0,row=3,padx=10)
        botonDetect.grid(column=0,row=4,padx=10)
        botonSegmentar.grid(column=0,row=5,padx=10)
        botonNotas.grid(column=0, row = 6, padx=10)
        Clicks+=1
    else:
        botonSegmentar.grid_remove()
        botonDetect.grid_remove()
        botonSelec.grid_remove()
        botonNotas.grid_remove()
        botonPaciente.grid_remove()
        Clicks=0
def guardar():
    global im
        # Abre una ventana de diálogo de selección de carpeta
    ruta_carpeta = filedialog.askdirectory()

    # Crea una imagen utilizando la biblioteca PIL
    imagen = im
    # Guarda la imagen en la carpeta seleccionada
    if len(entryNombre.get())>1:
        imagen.save(ruta_carpeta +'/'+entryNombre.get()+'.png')
        root.destroy()
    else:
        imagen.save('Imagen Trauma Solver.png')
        root.destroy()
def notas():
    global texto_ingresado, im
    txtnotas = tk.Tk()
    txtnotas.title("Notas quirurgicas")
    txtnotas.iconbitmap("./hueso.ico")
    # Función para guardar el texto ingresado en una variable
    def guardar_texto():
        global texto_ingresado
        texto_ingresado = cuadro_texto.get("1.0", "end-1c")
        print(texto_ingresado)
        txtnotas.destroy()

    # Widget de texto multilínea
    cuadro_texto = tk.Text(txtnotas, wrap="word", height=10)
    cuadro_texto.grid(row=0, column=0, padx=10, pady=10)

    # Botón de guardar
    boton_guardar = tk.Button(txtnotas, text="Guardar", command=guardar_texto)
    boton_guardar.grid(row=1, column=0, padx=10, pady=10)
def ayuda():
    ventAyuda = tk.Toplevel()
    ventAyuda.title('Ayuda')
    imageAyuda = Image.open('./Imagenes/ayuda.png')
    w,h = imageAyuda.size
    ventAyuda.geometry(str(w)+'x'+str(h))
    imageAyudaTk = ImageTk.PhotoImage(imageAyuda)
    tk.Label(ventAyuda, image=imageAyudaTk).place(x = 0, y = 0, relheight = 1, relwidth = 1)
    ventAyuda.mainloop()
def on_closing():
    if tk.messagebox.askokcancel("Cerrar ventana", "¿Estás seguro de que quieres cerrar la ventana?"):
        root.destroy()
"""def Implantes():
    ventImplant=tk.Toplevel()
    implante1"""


# Cargar imagen DICOM
ds = pydicom.dcmread('./Arce/ARCE0SM35Y.dcm')
# Convertir DICOM a Array
img = (ds.pixel_array)
# Normalizar los valores del array
imgNorm = (255-(img / img.max()*255)).astype('uint8')
# Crear imagen de array
scale_percent = 10 # percent of original size
width = int(imgNorm.shape[1] * scale_percent / 100)
height = int(imgNorm.shape[0] * scale_percent / 100)
dim = (width, height)
# Resize image
resized = cv2.resize(imgNorm, dim, interpolation = cv2.INTER_AREA)
# Crear imagen de PIL y PhotoImage de Tkinter
im = Image.fromarray(resized)
#Variables para Funciones
Clicks=0
texto_ingresado = ""
ClicksNotas=0
nombre=''

#Ventana Principal
root=tk.Tk()
root.title('Pagina Principal')
root.iconbitmap("./hueso.ico")
root.protocol("WM_DELETE_WINDOW", on_closing)


# Entrys globales
entryNombre=tk.Entry()
entryNombre2=tk.Entry()
entryEdad=tk.Entry()
entryEdad2=tk.Entry()
entryFecha=tk.Entry()
entryFecha2=tk.Entry()

#Contonedores 
vpButones=tk.Frame(root)
vpButones.grid(column=0,row=0,padx=10,pady=(10,10))
vpImagen=tk.Frame(root)
vpImagen.grid(column=0,row=1)
vpNotas=tk.Frame(root)
vpNotas.grid(column=0,row=2)


#Butones
botonEditar=ttk.Button(vpButones,text='Editar',command=herramientas)
botonEditar.grid(column=0,row=0,padx=(0,10))
botonClas=ttk.Button(vpButones,text='Clasificar',command=clasificar)
botonClas.grid(column=1,row=0,padx=(0,10))
botonImp=ttk.Button(vpButones,text='Implantes')
botonImp.grid(column=2,row=0,padx=(0,10))
botonSave=ttk.Button(vpButones,text='Guardar', command=guardar)
botonSave.grid(column=3,row=0,padx=(0,10))
botonHelp=ttk.Button(vpButones,text='Ayuda', command=ayuda)
botonHelp.grid(column=4,row=0,padx=(0,10))

#Botones Herramientas
botonSelec=ttk.Button(vpImagen,text='Seleccionar')
botonDetect=ttk.Button(vpImagen,text='Detectar pzas')
botonSegmentar=ttk.Button(vpImagen,text='Segmentar')
botonNotas = ttk.Button(vpImagen,text='Agregar notas', command = notas)
botonPaciente = ttk.Button(vpImagen,text='Info. Paciente',command=infoPaciente)

#Separador Botones
sBotones=ttk.Separator(root,orient='horizontal')
sBotones.grid

#Imagen
rx = ImageTk.PhotoImage(image=im)
canvas = tk.Canvas(vpImagen,width=width,height=height)
canvas.grid(column=1,row=1,rowspan=9,columnspan=8,sticky='nsew')
imagen=canvas.create_image(0, 0, image=rx, anchor=tk.NW)

# Main Loop
root.mainloop()



