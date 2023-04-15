from tkinter import *
import tkinter.font as tkFont

class Panel ():

    envio = False
    idFuncionB = None
    paquetesRecibidos = 0
    lista = []

    def __init__(self, vista):
        self.vista = vista
        self.img = PhotoImage(file="images/r2.png")

    def graficarNodo(self, listaNodos):
        self.limpiarCanvas()
        self.lista = listaNodos
        for i in listaNodos:

            a = Label(self.vista.panelDibujo , image = self.img, bd=0, text=i.id)
            a.place(x=i.corX, y=i.corY) 
            
            self.vista.panelDibujo.create_text(i.corX, i.corY-30,
                                                text="Nodo "+ str(i.id), fill="white")
            self.vista.controlMouse(a)
            
    def graficarLineas(self, nodo1, nodo2, distancia):
        
        self.vista.panelDibujo.create_line(nodo1[0], nodo1[1],
                                            nodo2[0], nodo2[1],
                                            fill="red", width=5)
        
        ubi = ((nodo1[0]+nodo2[0])/2,(nodo1[1]+nodo2[1])/2)
        self.vista.panelDibujo.create_text(ubi[0], ubi[1]-10, text=distancia, fill="white")

    

    def graficarPaquete(self, i):

        self.envio=True #Para que cuente la estadistica
        
        font1 = tkFont.Font(family="Times New Roman", size=8)
        
        paquete = Label(self.vista.panelDibujo, text=i.mensaje, bg="white",
                        fg="black", font=font1,  wraplength=40)

        self.vista.panelDibujo.create_window(i.corX, i.corY, window=paquete, tags=('Paquete'))
        
    
    def limpiarCanvas(self):

        self.vista.panelDibujo.delete("all")

        for widget in self.vista.panelDibujo.winfo_children():
            widget.destroy()