from tkinter import *
from tkinter import ttk
import tkinter as ttk

ventana = Tk()
ventana.geometry("1100x570")
ventana.title("Ejercicio_3")


# Crear frame principal
principal_Frame = ttk.Frame(ventana)
principal_Frame.grid()

#frame1
azul_Frame = ttk.Frame(principal_Frame, bg="#008080", relief="raised")
azul_Frame.grid(column=0, row=0, sticky=(W))

#contenido frame1
ttk.Label(azul_Frame, text="SPAI 4.0 ", bg="#008080", font=("Arial", 12), foreground="white").grid(column=1, row=0)
ttk.Label(azul_Frame, text="           ", bg="#008080", font=("Arial", 12, "bold"), foreground="#008080").grid(column=2, row=0, padx=452)

imagenlinea = PhotoImage(file= 'lineas.png')
imagen_linea = imagenlinea.subsample(80, 80) # La imagen se reducirá a la mitad en ambas direcciones (horizontal y vertical)
lineas_Imagen = ttk.Button(azul_Frame,bg="#008080",activebackground="#008080")
lineas_Imagen.grid(column=0, row=0,padx=30, pady=10)
lineas_Imagen['image']=imagen_linea
lineas_Imagen.config(borderwidth=0, highlightthickness=0)

#frame2
negro_Frame = ttk.Frame(principal_Frame, bg="#141414")
negro_Frame.grid(column=0, row=1)

#frame Auxiliar
aux_Frame = ttk.Frame(negro_Frame, bg="#141414")
aux_Frame.grid(column=0, row=0, padx=80, pady=5)

#frame3
tablas_Frame = ttk.Frame(aux_Frame, bg="#141414")
tablas_Frame.grid(column=0, row=0,padx=10, pady=5)

#frame3.1
Tabarriba_Frame = ttk.Frame(tablas_Frame, bg="#141414")
Tabarriba_Frame.grid(column=0, row=0)

#frame3.1.2
indicadores_Frame = ttk.Frame(Tabarriba_Frame, bg="#343434", relief="raised")
indicadores_Frame.grid(column=0, row=0,padx=5, pady=3)

#contenido_Indicadores
ttk.Label(indicadores_Frame, text="Indicadores Digitales \n ", bg="#343434", font=("Arial", 12, "bold"), foreground="#008080").grid(column=1, row=0, columnspan=4, padx=32)
ttk.Label(indicadores_Frame, text="Linea 1:          On\n ", bg="#343434", font=("Arial", 12, "bold"), foreground="white").grid(column=1, row=1, sticky=(W))
ttk.Label(indicadores_Frame, text="Linea 2:          On \n ", bg="#343434", font=("Arial", 12, "bold"), foreground="white").grid(column=1, row=2, sticky=(W))
ttk.Label(indicadores_Frame, text="Linea 1:          On \n ", bg="#343434", font=("Arial", 12, "bold"), foreground="white").grid(column=1, row=3, sticky=(W))
ttk.Label(indicadores_Frame, text="Gabinete: Abierto \n ", bg="#343434", font=("Arial", 12, "bold"), foreground="white").grid(column=1, row=4, sticky=(W))
ttk.Label(indicadores_Frame, text="Alarma:          On \n ", bg="#343434", font=("Arial", 12, "bold"), foreground="white").grid(column=1, row=5, sticky=(W))
ttk.Label(indicadores_Frame, text="Alarma 2:       Off\n ", bg="#343434", font=("Arial", 12, "bold"), foreground="white").grid(column=1, row=6, sticky=(W))

imagenbot = PhotoImage(file= 'circuloV.png')
imagen_redubo1= imagenbot.subsample(25)

bImagen = ttk.Label(indicadores_Frame, bg="#343434")
bImagen.grid(column=2, row=1, sticky=(N))
bImagen["image"]  = imagen_redubo1

imagenboto = PhotoImage(file= 'circuloV.png')
imagen_redubo2= imagenboto.subsample(25)

bomagen = ttk.Label(indicadores_Frame, bg="#343434")
bomagen.grid(column=2, row=2, sticky=(N))
bomagen["image"]  = imagen_redubo2

imagenboot = PhotoImage(file= 'circuloR.png')
imagen_redubo3= imagenboot.subsample(95)

bI2magen = ttk.Label(indicadores_Frame, bg="#343434")
bI2magen.grid(column=2, row=3, sticky=(N))
bI2magen["image"]  = imagen_redubo3

imagenbott = PhotoImage(file= 'circuloR.png')
imagen_redubo4= imagenbott.subsample(95)

bmagen = ttk.Label(indicadores_Frame, bg="#343434")
bmagen.grid(column=2, row=5, sticky=(N))
bmagen["image"]  = imagen_redubo4

imagennbot = PhotoImage(file= 'circuloV.png')
imagen_redubo5= imagennbot.subsample(25)

b6magen = ttk.Label(indicadores_Frame, bg="#343434")
b6magen.grid(column=2, row=6, sticky=(N))
b6magen["image"]  = imagen_redubo5

#frame3.1.2
temperaturas_Frame = Frame(Tabarriba_Frame, bg="#343434")
temperaturas_Frame.grid(column=1, row=0, sticky=(N), pady=3)

#contenido temperaturas
ttk.Label(temperaturas_Frame, text="Temperaturas \n ", bg="#343434", font=("Arial", 12, "bold"), foreground="#008080").grid(column=1, row=0)
ttk.Label(temperaturas_Frame, text="Temperatura 1: ", bg="#343434", font=("Arial", 10, "bold"), foreground="white").grid(column=1, row=1, pady=0)
ttk.Label(temperaturas_Frame, text="Temperatura 2: ", bg="#343434", font=("Arial", 10, "bold"), foreground="white").grid(column=2, row=1, pady=0)

imagentem = PhotoImage(file= '26 grados.png')
imagen_reducida1 = imagentem.subsample(3)

grdImagen = ttk.Label(temperaturas_Frame, bg="#343434")
grdImagen.grid(column=1, row=2,sticky=(N), pady=20, padx=14)
grdImagen["image"]  = imagen_reducida1

imagen60 = PhotoImage(file= '60grados.png')
imagen_reducida2 = imagen60.subsample(3)

grd60Imagen = ttk.Label(temperaturas_Frame, bg="#343434")
grd60Imagen.grid(column=2, row=2, sticky=(N), pady=20, padx=14)
grd60Imagen["image"]  = imagen_reducida2

ttk.Label(temperaturas_Frame, text="Temp. Agua: 58 °C", bg="#343434", font=("Arial", 10, "bold"), foreground="white").grid(column=1, row=3, pady=15,columnspan=2)
ttk.Label(temperaturas_Frame, text="Temp.Ambiente: 35° C", bg="#343434", font=("Arial", 10, "bold"), foreground="white").grid(column=1, row=4, pady=34,columnspan=2 )


#frame3.2
Tablabajo_Frame = ttk.Frame(tablas_Frame, bg="#141414")
Tablabajo_Frame.grid(column=0, row=1)
#frame3.2.1
bomba_Frame = ttk.Frame(Tablabajo_Frame, bg="#343434", relief="raised")
bomba_Frame.grid(column=0, row=0, pady=0, padx=0)

ttk.Label(bomba_Frame, text="Velocidad Bomba: ", bg="#343434", font=("Arial", 11, "bold"), foreground="white").grid(column=0, row=1, pady=25, padx=30)

imagenbom = PhotoImage(file= 'Bomba.png')
imagen_reducida3 = imagenbom.subsample( 2)

BImagen = ttk.Label(bomba_Frame, bg="#343434")
BImagen.grid(column=0, row=2,sticky=(N), padx=40, pady=10)
BImagen["image"]  = imagen_reducida3

#frame3.2.1
nivel_Frame = ttk.Frame(Tablabajo_Frame, bg="#343434", relief="raised")
nivel_Frame.grid(column=1, row=0, padx=8)

ttk.Label(nivel_Frame, text="Nivel del Tanque ", bg="#343434", font=("Arial", 10, "bold"), foreground="#008080").grid(column=0, row=1, pady=5, sticky=(W))

imagen85 = PhotoImage(file= '85.png')
imagen_reducida4 = imagen85.subsample(2)

nivmagen = ttk.Label(nivel_Frame, bg="#343434")
nivmagen.grid(column=0, row=2,sticky=(N), padx=18)
nivmagen["image"]  = imagen_reducida4


#frame4
grafica_Frame = ttk.Frame(aux_Frame, bg="#343434", relief="raised")
grafica_Frame.grid(column=1, row=0, sticky=(N), pady=8)#aprender a saber centrarlo

ttk.Label(grafica_Frame, text="Produccion ", bg="#343434", font=("Arial", 12, "bold"), foreground="#008080").grid(column=0, row=1, sticky=(W))

imagengra = PhotoImage(file= 'grafica.png')
imagen_reducida5 = imagengra.subsample(2, 2)

gramagen = ttk.Label(grafica_Frame, bg="#343434")
gramagen.grid(column=0, row=2,sticky=(N))
gramagen["image"]  = imagen_reducida5

ttk.Label(grafica_Frame, text="Piezas producidas: 50 ", bg="#343434", font=("Arial", 10, "bold"), foreground="white").grid(column=0, row=3, pady=20)
ttk.Label(grafica_Frame, text="Piezas defectuosas: 12 ", bg="#343434", font=("Arial", 10, "bold"), foreground="white").grid(column=0, row=4, pady=20)

# Mostrar ventana
ventana.mainloop()