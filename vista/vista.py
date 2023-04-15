from tkinter import *
from tkinter import ttk
import sys

import tkinter.font as tkFont
from controlador import Controller as c
from modelo import Logic as lg

class vista:
    ventana = Tk()
    ventana.title("Simulacion Red Ad-Hoc")
    ventana.geometry("1050x600")
    
    listaNodos = []

    def __init__(self):
        self.ruido = IntVar()
        self.anchob = IntVar()
        self.control = c.Controlador(lg.Logica(self),self)
        self.initFrame()
        self.initLabels()
        self.initSlider()
        self.initButtons()
        self.initEntrada()

    def initFrame(self):
        self.panelPrincipal = Frame(self.ventana, bg="#0A1915")
        self.panelPrincipal.pack(fill=BOTH, expand=True)

        self.panelDibujo =  Canvas(self.panelPrincipal,highlightthickness=2,bg="black", highlightbackground="#0A1915")
        self.panelDibujo.place(x=460, y=100, width=400, height=380)
        

    def initLabels(self):
        #Titulo
        font1 = tkFont.Font(family="Press Start 2P Regular", size=12)
        l1 = Label(self.panelPrincipal, text="Simulación Red Ad-Hoc",bg="#0A1915", fg="#F54E00",font=font1)
        l1.place(x=325,y=10,width=350,height=50)

        #Autores
        font1 = tkFont.Font(family="Consolas", size=12)
        l2 = Label(self.ventana, text="Juan Arias, Camilo Hernandez, David Jimenez, Juan Varon",bg="#0A1915",  fg="#F54E00", font=font1)
        l2.place(x=250,y=50,width=520,height=15)

        #Interferencia
        font1 = tkFont.Font(family="Press Start 2P Regular", size=9)
        l2 = Label(self.ventana, text="Latencia de red",bg="#0A1915",  fg="#FC9B09", font=font1)
        l2.place(x=20,y=100,width=180,height=15)

        #Ancho de banda
        l2 = Label(self.ventana, text="Ancho de banda",bg="#0A1915",  fg="#FC9B09", font=font1)
        l2.place(x=20,y=190,width=180,height=15)

        #Etiqueta para enviar paquete
        l2 = Label(self.ventana, text="Escribe un mensaje!",bg="#0A1915",  fg="#FC9B09", font=font1)
        l2.place(x=20,y=340,width=240,height=18)

        font1 = tkFont.Font(family="Press Start 2P Regular", size=10)
        l2 = Label(self.ventana, text="Nodo salida",bg="black",  fg="#FC9B09", font=font1)
        l2.place(x=20, y=410,width=200,height=26)

        l2 = Label(self.ventana, text="Nodo llegada",bg="black",  fg="#FC9B09", font=font1)
        l2.place(x=20, y=450,width=200,height=26)

        #Trafico
        font1 = tkFont.Font(family="Press Start 2P Regular", size=7)
        l2 = Label(self.ventana, text="Trafico",bg="#1F0802",  fg="white", font=font1)
        l2.place(x=880,y=100,width=150,height=35)

        self.ltrafico = Label(self.ventana, text="BAJO",bg="white",  fg="black", font=font1)
        self.ltrafico.place(x=880,y=135,width=150,height=30)
        
        #Distancia promedio
        font1 = tkFont.Font(family="Press Start 2P Regular", size=7)
        l2 = Label(self.ventana, text="Distancia\nPromedio",bg="#1F0802",  fg="white", font=font1)
        l2.place(x=880,y=200,width=150,height=35)

        self.ldist = Label(self.ventana, text="0",bg="white",  fg="black", font=font1)
        self.ldist.place(x=880,y=235,width=150,height=30)

        #Tasa de envio
        font1 = tkFont.Font(family="Press Start 2P Regular", size=7)
        l2 = Label(self.ventana, text="Tasa de\nenvio",bg="#1F0802",  fg="white", font=font1)
        l2.place(x=880,y=300,width=150,height=35)

        self.tenvio = Label(self.ventana, text="0",bg="white",  fg="black", font=font1)
        self.tenvio.place(x=880,y=335,width=150,height=30)

        #tasa de recibido
        font1 = tkFont.Font(family="Press Start 2P Regular", size=7)
        l2 = Label(self.ventana, text="Tasa de\nRecibido",bg="#1F0802",  fg="white", font=font1)
        l2.place(x=880,y=400,width=150,height=35)

        self.trecibido = Label(self.ventana, text="0",bg="white",  fg="black", font=font1)
        self.trecibido.place(x=880,y=435,width=150,height=30)

        

    def initSlider(self):
        
        self.inter = Scale(self.panelPrincipal, from_=0, to=100, orient= HORIZONTAL,
                       length=400, variable=self.ruido, bg="#0A1915",fg="white",  highlightbackground="#0A1915",
                       showvalue=True, tickinterval=20)
        self.inter.place(x=20,y=120)

        self.ancho = Scale(self.panelPrincipal, from_=40, to=100, orient= HORIZONTAL,
                       length=400, variable=self.anchob, bg="#0A1915",fg="white",  highlightbackground="#0A1915",
                       showvalue=True, tickinterval=20)
        self.ancho.place(x=20,y=200)
    

    def initButtons(self):
        font1 = tkFont.Font(family="Press Start 2P Regular", size=8)

        botonAgregar = Button(self.panelPrincipal, text="Agregar Nodo",height=2, width=16,bg="#F54E00",
                               fg="black",font =font1, command=lambda: self.control.realizarOp("agregar"))
        botonAgregar.place(x=20,y=280)

        botonEliminar = Button(self.panelPrincipal, text="Eliminar Nodo",height=2, width=16,bg="#F54E00",
                               fg="black",font =font1, command=lambda: self.control.realizarOp("eliminar"))
        botonEliminar.place(x=235,y=280)

        font1 = tkFont.Font(family="Press Start 2P Regular", size=9)
        botonAleatoria = Button(self.panelPrincipal, text="Aleatorio",height=2, width=23,bg="#F54E00",
                               fg="black", font =font1,command=lambda: self.control.realizarOp("aleatoriamente"))
        botonAleatoria.place(x=460,y=500)

        botonDetener = Button(self.panelPrincipal, text="Detener",height=2, width=20,bg="#F54E00",
                               fg="black", font =font1,command=lambda: self.control.realizarOp("detener"))
        botonDetener.place(x=780,y=500)

        botonEnviar = Button(self.panelPrincipal, text="Enviar", height=2, width=27, bg="#F54E00", 
                               fg="black",font =font1, command=lambda: self.control.realizarOp("enviar"))
        botonEnviar.place(x=20, y=500)

    
    def initEntrada(self):
        font1 = tkFont.Font(family="Times New Roman", size=14)
        self.mensaje = Entry(self.panelPrincipal, width=44, font= font1,justify='center')
        self.mensaje.place(x=20, y=370)

        self.nSalida = Entry(self.panelPrincipal, width=14, font= font1,justify='center')
        self.nSalida.place(x=220, y=410)
        
        self.nLlegada = Entry(self.panelPrincipal, width=14, font= font1,justify='center')
        self.nLlegada.place(x=220, y=450)
                
        

    def controlMouse(self, item):
        item.bind("<B1-Motion>", self.control.arrastrarEti)
        item.bind("<ButtonRelease-1>", self.control.soltarEti)
        self.listaNodos.append(item)
        
    def actualizarControl(self, controlador):
        self.control = controlador
