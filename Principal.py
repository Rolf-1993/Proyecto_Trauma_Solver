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
        boton31A11 = tk.Button(clasificacion, text = '31A1.1', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton31A11.cget('text')))
        boton31A11.place(x=157+9,y=82+9)
        boton31A12 = tk.Button(clasificacion, text = '31A1.2', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton31A12.cget('text')))
        boton31A12.place(x=157+9,y=230+9)
        boton31A13 = tk.Button(clasificacion, text = '31A1.3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton31A13.cget('text')))
        boton31A13.place(x=157+9,y=381+9)
        boton31A22 = tk.Button(clasificacion, text = '31A2.2', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg ='#000000', bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton31A22.cget('text')))
        boton31A22.place(x=157+9,y=527+9)
        boton31A23 = tk.Button(clasificacion, text = '31A2.3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton31A23.cget('text')))
        boton31A23.place(x=330+166,y=82+10)
        boton31A31 = tk.Button(clasificacion, text = '31A3.1', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton31A31.cget('text')))
        boton31A31.place(x=330+166,y=230+10)
        boton31A32 = tk.Button(clasificacion, text = '31A3.2', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton31A32.cget('text')))
        boton31A32.place(x=330+166,y=381+10)
        boton31A33 = tk.Button(clasificacion, text = '31A3.3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton31A33.cget('text')))
        boton31A33.place(x=330+166,y=527+10)
        botonRegresar = tk. Button (clasificacion, text = 'Regresar', font = ('Canva Sans', 17,'bold'),  fg='#ffffff', bg = '#4a4a4a', cursor='hand2', command= vent31)
        botonRegresar.place(x=0,y=0)
    def vent31B ():
        tk.Label(clasificacion, image=fondo31Btk ).place(x = 0, y = 0, relheight = 1, relwidth = 1)
        boton31B11 = tk.Button(clasificacion, text = '31B1.1', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton31B11.cget('text')))
        boton31B11.place(x=157+9,y=82+9)
        boton31B12 = tk.Button(clasificacion, text = '31B1.2', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton31B12.cget('text')))
        boton31B12.place(x=157+9,y=230+9)
        boton31B13 = tk.Button(clasificacion, text = '31B1.3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton31B13.cget('text')))
        boton31B13.place(x=157+9,y=381+9)
        boton31B21 = tk.Button(clasificacion, text = '31B2.1', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg ='#000000', bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton31B21.cget('text')))
        boton31B21.place(x=157+9,y=527+9)
        boton31B22 = tk.Button(clasificacion, text = '31B2.2', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton31B21.cget('text')))
        boton31B22.place(x=330+166,y=82+10)
        boton31B33 = tk.Button(clasificacion, text = '31B2.3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton31B33.cget('text')))
        boton31B33.place(x=330+166,y=230+10)
        boton31B3 = tk.Button(clasificacion, text = '31B3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton31B3.cget('text')))
        boton31B3.place(x=330+166,y=381+10)
        botonRegresar = tk. Button (clasificacion, text = 'Regresar', font = ('Canva Sans', 17,'bold'),  fg='#ffffff', bg = '#4a4a4a', cursor='hand2', command=vent31)
        botonRegresar.place(x=0,y=0)   
    def vent31C ():
        tk.Label(clasificacion, image=fondo31Ctk ).place(x = 0, y = 0, relheight = 1, relwidth = 1)
        boton31C11 = tk.Button(clasificacion, text = '31C1.1', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton31C11.cget('text')))
        boton31C11.place(x=157+9,y=82+9)
        boton31C12 = tk.Button(clasificacion, text = '31C1.2', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton31C12.cget('text')))
        boton31C12.place(x=157+9,y=230+9)
        boton31C13 = tk.Button(clasificacion, text = '31C1.3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton31C13.cget('text')))
        boton31C13.place(x=157+9,y=381+9)
        boton31C21 = tk.Button(clasificacion, text = '31C2.1', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg ='#000000', bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton31C21.cget('text')))
        boton31C21.place(x=157+9,y=527+9)
        boton31C22 = tk.Button(clasificacion, text = '31C2.2', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton31C22.cget('text')))
        boton31C22.place(x=330+166,y=82+10)
        boton31C23 = tk.Button(clasificacion, text = '31C2.3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton31C23.cget('text')))
        boton31C23.place(x=330+166,y=230+10)
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
        botonSpiral = tk.Button(clasificacion, text = 'En espiral', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2',command=lambda:ClasFinal(botonSpiral.cget('text')))
        botonOblique = tk.Button(clasificacion, text = 'Oblicua (>30°)', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2',command=lambda:ClasFinal(botonOblique.cget('text')))
        botonTransverse = tk.Button(clasificacion, text = 'Transversal (<30°)', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2',command=lambda:ClasFinal(botonTransverse.cget('text')))
        botonSpiral.place(x=280,y=122)
        botonOblique.place(x=260,y=330)
        botonTransverse.place(x=240,y=530)
        botonRegresar = tk. Button (clasificacion, text = 'Regresar', font = ('Canva Sans', 17,'bold'),  fg='#ffffff', bg = '#4a4a4a', cursor='hand2', command=vent32)
        botonRegresar.place(x=0,y=0)
    def vent32B ():
        tk.Label(clasificacion, image=fondo32Btk ).place(x = 0, y = 0, relheight = 1, relwidth = 1)
        botonIntact32B = tk.Button(clasificacion, text = ' Cuña intacta', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2',command=lambda:ClasFinal(botonIntact32B.cget('text')))
        botonFragment32B = tk.Button(clasificacion, text = 'Cuña fragmentaria', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2',command=lambda:ClasFinal(botonFragment32B.cget('text')))
        botonIntact32B.place(x=250,y=160)
        botonFragment32B.place(x=222,y=465)
        botonRegresar = tk. Button (clasificacion, text = 'Regresar', font = ('Canva Sans', 17,'bold'),  fg='#ffffff', bg = '#4a4a4a', cursor='hand2', command=vent32)
        botonRegresar.place(x=0,y=0)
    def vent32C ():
        tk.Label(clasificacion, image=fondo32Ctk ).place(x = 0, y = 0, relheight = 1, relwidth = 1)
        botonIntact32C = tk.Button(clasificacion, text = ' Segmentaria intacta', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2',command=lambda:ClasFinal(botonIntact32C.cget('text')))
        botonFragment32C = tk.Button(clasificacion, text = 'Segmentaria fragmentaria', relief= 'flat', font=('Canva Sans', 17), bg ='#b2b2b2', cursor='hand2',command=lambda:ClasFinal(botonFragment32C.cget('text')))
        botonIntact32C.place(x=215,y=160)
        botonFragment32C.place(x=184,y=465)
        botonRegresar = tk. Button (clasificacion, text = 'Regresar', font = ('Canva Sans', 17,'bold'),  fg='#ffffff', bg = '#4a4a4a', cursor='hand2', command=vent32)
        botonRegresar.place(x=0,y=0)
    def vent33 ():
        tk.Label(clasificacion, image=fondo33tk).place(x = 0, y = 0, relheight = 1, relwidth = 1)
        botonExtra = tk.Button(clasificacion, text = 'Extraarticular', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2',command=vent33A)
        botonArtPar = tk.Button(clasificacion, text = 'Articular parcial', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2',command=vent33B)
        botonArtComp = tk.Button(clasificacion, text = 'Articular completa', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2',command=vent33C)
        botonRegresar = tk. Button (clasificacion, text = 'Regresar', font = ('Canva Sans', 17,'bold'),  fg='#ffffff', bg = '#4a4a4a', cursor='hand2', command=regvent30)
        botonRegresar.place(x=0,y=0)
        botonExtra.place(x=255,y=120)
        botonArtPar.place(x=250,y=325)
        botonArtComp.place(x=240,y=530)
    def vent33A ():
        tk.Label(clasificacion, image=fondo33Atk ).place(x = 0, y = 0, relheight = 1, relwidth = 1)
        boton33A11 = tk.Button(clasificacion, text = '33A1.1', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton33A11.cget('text')))
        boton33A11.place(x=157+9,y=82+9)
        boton33A12 = tk.Button(clasificacion, text = '33A1.2', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton33A12.cget('text')))
        boton33A12.place(x=157+9,y=230+9)
        boton33A13 = tk.Button(clasificacion, text = '33A1.3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton33A13.cget('text')))
        boton33A13.place(x=157+9,y=381+9)
        boton33A22 = tk.Button(clasificacion, text = '33A2.2', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg ='#000000', bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton33A22.cget('text')))
        boton33A22.place(x=157+9,y=527+9)
        boton33A23 = tk.Button(clasificacion, text = '33A2.3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton33A23.cget('text')))
        boton33A23.place(x=330+166,y=82+10)
        boton33A31 = tk.Button(clasificacion, text = '33A3.1', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton33A31.cget('text')))
        boton33A31.place(x=330+166,y=230+10)
        boton33A32 = tk.Button(clasificacion, text = '33A3.2', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton33A32.cget('text')))
        boton33A32.place(x=330+166,y=381+10)
        boton33A33 = tk.Button(clasificacion, text = '33A3.3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton33A33.cget('text')))
        boton33A33.place(x=330+166,y=527+10)
        botonRegresar = tk. Button (clasificacion, text = 'Regresar', font = ('Canva Sans', 17,'bold'),  fg='#ffffff', bg = '#4a4a4a', cursor='hand2', command= vent33)
        botonRegresar.place(x=0,y=0)
    def vent33B ():
        tk.Label(clasificacion, image=fondo33Btk ).place(x = 0, y = 0, relheight = 1, relwidth = 1)
        boton33B11 = tk.Button(clasificacion, text = '33B1.1', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton33B11.cget('text')))
        boton33B11.place(x=170,y=82+9)
        boton33B12 = tk.Button(clasificacion, text = '33B1.2', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton33B12.cget('text')))
        boton33B12.place(x=180,y=230+9)
        boton33B13 = tk.Button(clasificacion, text = '33B1.3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton33B13.cget('text')))
        boton33B13.place(x=180,y=381+9)
        boton33B21 = tk.Button(clasificacion, text = '33B2.1', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg ='#000000', bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton33B21.cget('text')))
        boton33B21.place(x=180,y=527+9)
        boton33B22 = tk.Button(clasificacion, text = '33B2.2', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton33B22.cget('text')))
        boton33B22.place(x=502,y=82+10)
        boton33B23 = tk.Button(clasificacion, text = '33B3.3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton33B23.cget('text')))
        boton33B23.place(x=512,y=230+10)
        boton33B31 = tk.Button(clasificacion, text = '33B3.1', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton33B31.cget('text')))
        boton33B31.place(x=512,y=381+10)
        boton33B33 = tk.Button(clasificacion, text = '33B3.3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton33B33.cget('text')))
        boton33B33.place(x=512,y=527+10)
        botonRegresar = tk. Button (clasificacion, text = 'Regresar', font = ('Canva Sans', 17,'bold'),  fg='#ffffff', bg = '#4a4a4a', cursor='hand2', command= vent33)
        botonRegresar.place(x=0,y=0)
    def vent33C ():
        tk.Label(clasificacion, image=fondo33Ctk ).place(x = 0, y = 0, relheight = 1, relwidth = 1)
        boton33C11 = tk.Button(clasificacion, text = '33C1.1', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton33C11.cget('text')))
        boton33C11.place(x=157+9,y=82+9)
        boton33C13 = tk.Button(clasificacion, text = '33C1.3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton33C13.cget('text')))
        boton33C13.place(x=157+9,y=230+9)
        boton33C21 = tk.Button(clasificacion, text = '33C2.1', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton33C21.cget('text')))
        boton33C21.place(x=157+9,y=381+9)
        boton33C22 = tk.Button(clasificacion, text = '33C2.2', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg ='#000000', bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton33C22.cget('text')))
        boton33C22.place(x=157+9,y=527+9)
        boton33C23 = tk.Button(clasificacion, text = '33C2.3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton33C23.cget('text')))
        boton33C23.place(x=330+166,y=82+10)
        boton33C31 = tk.Button(clasificacion, text = '33C3.1', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton33C31.cget('text')))
        boton33C31.place(x=330+166,y=230+10)
        boton33C32 = tk.Button(clasificacion, text = '33C3.2', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton33C32.cget('text')))
        boton33C32.place(x=330+166,y=381+10)
        boton33C33 = tk.Button(clasificacion, text = '33C3.3', relief= 'flat', font=('Canva Sans', 14, 'bold'), fg='#000000' , bg ='#e1e1e1', cursor='hand2',command=lambda:ClasFinal(boton33C33.cget('text')))
        boton33C33.place(x=330+166,y=527+10)
        botonRegresar = tk. Button (clasificacion, text = 'Regresar', font = ('Canva Sans', 17,'bold'),  fg='#ffffff', bg = '#4a4a4a', cursor='hand2', command= vent33)
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
    # Fondo clase 32A
    fondo32A = Image.open('./Fondos/ClasSubDiaf32A.png')
    fondo32Atk = ImageTk.PhotoImage(fondo32A)
    # Fondo clase 32B
    fondo32B = Image.open('./Fondos/ClasSubDiaf32B.png')
    fondo32Btk = ImageTk.PhotoImage(fondo32B)
    # Fondo clase 32C
    fondo32C = Image.open('./Fondos/ClasSubDiaf32C.png')
    fondo32Ctk = ImageTk.PhotoImage(fondo32C)
    # Fondo clase 33
    fondo33 = Image.open('./Fondos/ClasDistal.png')
    fondo33tk = ImageTk.PhotoImage(fondo33)
    # Fondo clase 33A
    fondo33A = Image.open('./Fondos/ClasSubDist33A.png')
    fondo33Atk = ImageTk.PhotoImage(fondo33A)
    # Fondo clase 33B
    fondo33B = Image.open('./Fondos/ClasSubDist33B.png')
    fondo33Btk = ImageTk.PhotoImage(fondo33B)
    # Fondo clase 33C
    fondo33C = Image.open('./Fondos/ClasSubDist33C.png')
    fondo33Ctk = ImageTk.PhotoImage(fondo33C)
    

    
    tk.Label(clasificacion, image=fondo30stk).place(x = 0, y = 0, relheight = 1, relwidth = 1)
    # Botones Clas30s
    botonSegProx = tk.Button(clasificacion, text = 'Segmento proximal',relief ='flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2', command= vent31)
    botonSegProx.place(x=240,y=122)
    botonDiaf = tk.Button(clasificacion, text = 'Diáfisis', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2',command=vent32)
    botonDiaf.place(x=310,y=325)
    botonSegDist = tk.Button(clasificacion, text = 'Segmento distal', relief= 'flat', font=('Canva Sans', 18), bg ='#b2b2b2', cursor='hand2',command=vent33)
    botonSegDist.place(x=260,y=540)

    clasificacion.mainloop()
def infoPaciente():
    global entryNombre, entryNombre2, entryFecha, entryFecha2, entryEdad, entryEdad2, ClicksNotas, custom_font
    def TerminarPaciente():
        paciente.withdraw()
    paciente=tk.Toplevel()
    paciente.title('Información del Paciente')
    paciente.iconbitmap("./hueso.ico")
    #Etiquetas
    nombrePaciente=tk.Label(paciente,text='Nombre del Paciente:', font=custom_font)
    nombrePaciente.grid(column=0,row=0,pady=(10,0))
    edadPaciente=tk.Label(paciente,text='Edad del Paciente', font=custom_font)
    edadPaciente.grid(column=0,row=1,pady=(10,0))
    fecha=tk.Label(paciente,text='Fecha:', font=custom_font)
    fecha.grid(column=0,row=2)
    #Buton
    botonListo=tk.Button(paciente,text='Listo',command=TerminarPaciente, font=custom_font)
    botonListo.grid(column=0,row=5, pady=(20,20),padx=(130,0))

    if ClicksNotas==0:
        entryNombre=tk.Entry(paciente, font=custom_font)
        entryNombre.insert(0,entryNombre2.get())
        entryNombre.grid(column=1,row=0,pady=(10,0), padx=(0,10))
        entryEdad=tk.Entry(paciente, font=custom_font)
        entryEdad.insert(0,entryEdad2.get())
        entryEdad.grid(column=1,row=1,pady=(10,0), padx=(0,10))
        entryFecha=tk.Entry(paciente, font=custom_font)
        entryFecha.insert(0,entryFecha2.get())
        entryFecha.grid(column=1,row=2,pady=(10,0), padx=(0,10))
        ClicksNotas+=1
    else:
        entryNombre2 = tk.Entry(paciente, font=custom_font)
        entryNombre2.insert(0,entryNombre.get())
        entryNombre2.grid(column=1,row=0,pady=(10,0), padx=(0,10))
        entryEdad2 = tk.Entry(paciente, font=custom_font)
        entryEdad2.insert(0,entryEdad.get())
        entryEdad2.grid(column=1,row=1, padx=(0,10))
        entryFecha2=tk.Entry(paciente, font=custom_font)
        entryFecha2.insert(0,entryFecha.get())
        entryFecha2.grid(column=1,row=2,pady=(10,0), padx=(0,10))
        ClicksNotas=0
def area_seleccion():
    global rect, contador_clicks
    respuesta = messagebox.askquestion('Area seleccion', '¿Estás seguro de que esta es el área correcta?')
    if respuesta == 'yes':
        canvas.delete(rect)
        contador_clicks=0
    else:
        canvas.delete(rect)
        contador_clicks=0
        BotonRect()      
def rectangulo(event):
    global x1,y1,x2,y2,contador_clicks,h,w, rect
    if contador_clicks==0:
        x1=event.x
        y1=event.y
        contador_clicks+=1
    elif contador_clicks==1:
        x2=event.x
        y2=event.y
        contador_clicks+=1
        h=y2-y1
        w=x2-x1
        rect = canvas.create_rectangle(x1, y1, x1+w, y1+h, fill='blue', stipple='gray25')
        canvas.itemconfig(rect, fill="#0000FF")
        area_seleccion()
def BotonRect():
    canvas.bind("<Button-1>",rectangulo)
def herramientas():
    print("Ancho:", root.winfo_width(), "Alto:", root.winfo_height())
    global Clicks
    #Botones Herramientas
    if Clicks==0:
        botonPaciente.grid(column=0, row = 2, padx=(20,5), pady=(30,10))
        botonSelec.grid(column=0,row=3,padx=(20,5), pady=(0,10))
        botonDetect.grid(column=0,row=4,padx=(20,5), pady=(0,10))
        botonSegmentar.grid(column=0,row=5,padx=(20,5), pady=(0,10))
        botonNotas.grid(column=0, row = 6, padx=(20,5))
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
    global texto_ingresado, custom_font
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
    cuadro_texto = tk.Text(txtnotas, wrap="word", height=10, font=custom_font)
    cuadro_texto.grid(row=0, column=0, padx=10, pady=10)

    # Botón de guardar
    boton_guardar = tk.Button(txtnotas, text="Guardar", command=guardar_texto, font=custom_font)
    boton_guardar.grid(row=1, column=0, padx=10, pady=10)
def SubirArchivo():
    global rx,im
    botonSelecArchivo.destroy()
    file_path=filedialog.askopenfilename()
    # Cargar imagen DICOM
    ds = pydicom.dcmread(file_path)
    # Convertir DICOM a Array
    img = (ds.pixel_array)
    # Normalizar los valores del array
    imgNorm = (255-(img / img.max()*255)).astype('uint8')
    # Crear imagen de array
    scale_percent = 20 # percent of original size
    width = int(imgNorm.shape[1] * scale_percent / 100)
    height = int(imgNorm.shape[0] * scale_percent / 100)
    dim = (width, height)
    # Resize image
    resized = cv2.resize(imgNorm, dim, interpolation = cv2.INTER_AREA)
    # Crear imagen de PIL y PhotoImage de Tkinter
    im = Image.fromarray(resized)
    #Imagen
    rx = ImageTk.PhotoImage(im)
    canvas.itemconfig(imagen, image=rx)
    """canvas = tk.Canvas(vpImagen,width=width,height=height)
    canvas.grid(column=1,row=1,rowspan=9,columnspan=8,sticky='nsew')
    canvas.create_image(0, 0, image=rx, anchor=tk.NW)"""
    #tk.Label(canvas, image= rx)
def ayuda():
    ventAyuda = tk.Toplevel()
    ventAyuda.title('Ayuda')
    imageAyuda = Image.open('./Imagenes/ayuda.png')
    w,h = imageAyuda.size
    ventAyuda.geometry(str(w)+'x'+str(h))
    imageAyudaTk = ImageTk.PhotoImage(imageAyuda)
    tk.Label(ventAyuda, image=imageAyudaTk).place(x = 0, y = 0, relheight = 1, relwidth = 1)
    ventAyuda.iconbitmap("./hueso.ico")
    ventAyuda.mainloop()
def on_closing():
    if tk.messagebox.askokcancel("Cerrar ventana", "¿Estás seguro de que quieres cerrar la ventana?"):
        root.destroy()

#Variables para Funciones
Clicks=0
texto_ingresado = ""
ClicksNotas=0
nombre=''
contador_clicks = 0
custom_font = ('Helvetica', 14)

#Ventana Principal
root=tk.Tk()
root.title('Pagina Principal')
root.protocol("WM_DELETE_WINDOW", on_closing)
root.iconbitmap("./hueso.ico")

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
vpExtras=tk.Frame(root)
vpExtras.grid(column=0,row=3)

#Butones
s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 16,'bold'))
botonEditar=ttk.Button(vpButones,text='Editar',command=herramientas,style='my.TButton')
botonEditar.grid(column=0,row=0,padx=(53,50))
botonClas=ttk.Button(vpButones,text='Clasificar',command=clasificar,style='my.TButton')
botonClas.grid(column=1,row=0,padx=(0,50))
botonImp=ttk.Button(vpButones,text='Implantes',style='my.TButton')
botonImp.grid(column=2,row=0,padx=(0,50))
botonSave=ttk.Button(vpButones,text='Guardar', command=guardar,style='my.TButton')
botonSave.grid(column=3,row=0,padx=(0,50))
botonHelp=ttk.Button(vpButones,text='Ayuda',style='my.TButton',command=ayuda)
botonHelp.grid(column=4,row=0,padx=(0,50))
botonSelecArchivo=ttk.Button(vpExtras,text='Seleccionar archivo', command=SubirArchivo,style='my.TButton')
botonSelecArchivo.grid(column=2,row=0,padx=(10,10), pady=(10,15))

#Botones Herramientas
botonSelec=ttk.Button(vpImagen,text='Seleccionar',style='my.TButton', command=BotonRect)
botonDetect=ttk.Button(vpImagen,text='Detectar pzas',style='my.TButton')
botonSegmentar=ttk.Button(vpImagen,text='Segmentar',style='my.TButton')
botonNotas = ttk.Button(vpImagen,text='Agregar notas',style='my.TButton', command = notas)
botonPaciente = ttk.Button(vpImagen,text='Info. Paciente', style='my.TButton', command=infoPaciente)

#Separador Botones
sBotones=ttk.Separator(root,orient='horizontal')
sBotones.grid

#Imagen

# Cargar imagen de fondo
img = cv2.imread('./Fondos/imagen_inicial.png')
# Crear imagen de array
scale_percent = 100 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# Resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
# Crear imagen de PIL y PhotoImage de Tkinter
im = Image.fromarray(resized)
rx = ImageTk.PhotoImage(image=im)
canvas = tk.Canvas(vpImagen,width=width,height=height)
canvas.grid(column=1,row=1,columnspan=8,rowspan=9)
imagen=canvas.create_image(0, 0, image=rx, anchor=tk.NW)

# Main Loop
root.mainloop()

