import math
import random
import numpy as np
from tkinter import *
from modelo import Nodo as n
from vista import Panel as pa
from modelo import Paquete as pq

class Logica:
    
    auxiliar = 1
    validar = False
    idFuncionA = None
    tTranscurrido = 1
    paquetesEnviados = 0
    paquetesRecibidos = 0

    def __init__(self, vistaPrincipal):
        self.nodos = []
        self.paquetes = []
        self.distancias = []
        self.vistaPrincipal = vistaPrincipal
        self.panel = pa.Panel(vistaPrincipal)
        self.imagen_original = PhotoImage(file="images/r2.png")

    def agregarNodo(self):
        if(len(self.nodos)<4):
            x, y = random.randint(0, 350), random.randint(0, 300)
            xd, yd = random.randint(0, 350), random.randint(0, 300)
            id = len(self.nodos)
            self.nodos.append(n.Nodo(x,y,id,(xd,yd)))
            self.rePaint()

    def crearConexion(self):
        self.delConexiones()
        tamaño = len(self.nodos)
        if 1 < tamaño <= 3:
            for i in range(tamaño):
                for j in range(1, tamaño):
                    self.nodos[i].conexiones.append(self.nodos[i-j].id)
        elif tamaño >= 4:
            for i, item in enumerate(self.nodos):
                if i in (0, 3):
                    item.conexiones.extend((self.nodos[1].id, self.nodos[2].id))
                else:
                    item.conexiones.extend((self.nodos[0].id, self.nodos[3].id))

    def eliminarNodo(self):
        if(len(self.nodos)>0):
            id = self.nodos.pop(len(self.nodos)-1).id
            self.vistaPrincipal.listaNodos.pop(len(self.vistaPrincipal.listaNodos)-1)
            for i in self.nodos:
                if(id in i.conexiones):
                    i.conexiones.remove(id)
        self.rePaint()

    def moverNodo(self, x, y, label):
        label.place(x = label.winfo_x()+x, y = label.winfo_y()+y)
    
    def moverAleatorio(self):
        self.validar=True
        for i in self.nodos:
            a = Label(self.vistaPrincipal.panelDibujo , image = self.panel.img, bd=0, text=i.id)
            
            a.place(x=i.corX, y=i.corY) 
            
            self.vistaPrincipal.panelDibujo.create_text(i.corX, i.corY-30,
                                                    text="Nodo "+ str(i.id), fill="white")
    
            if(abs(i.corX - i.destino[0]) <= 5 and abs(i.corY - i.destino[1]) <= 5):
                i.destino = (random.randint(0, 350), random.randint(0, 300))
            else:
                if i.corX is not i.destino[0]:
                    i.corX += 1 if i.corX < i.destino[0] else -1
                if i.corY is not i.destino[1]:
                    i.corY += 1 if i.corY < i.destino[1] else -1
        
        if(self.panel.envio):
            self.tTranscurrido += 100
            self.actualizarDatos(self.tTranscurrido)

        self.actualizarRecorrido()
        self.rePaint()
        self.idFuncionA = self.vistaPrincipal.panelDibujo.after(50, self.moverAleatorio)

    def actualizarRecorrido(self):
        for pq in self.paquetes:
            for nodo in pq.recorrido:
                nodo.corX = self.nodos[nodo.id].corX
                nodo.corY = self.nodos[nodo.id].corY
            pq.ruta = self.calcularRuta(pq.recorrido)
    
    def crearLineas(self, lista):
        self.distancias = []
        tamaño = len(lista)
        if tamaño > 1:
            for nodo in lista:
                nodo.distancias = {}
                for idCon in nodo.conexiones:
                    nodo1 = (nodo.corX, nodo.corY)
                    nodo2 = (lista[idCon].corX, lista[idCon].corY)
                    distancia = int(math.dist(nodo1,nodo2))
                    nodo.distancias[idCon] = distancia
                    self.panel.graficarLineas(nodo1, nodo2, distancia)
                    if distancia not in self.distancias:
                        self.distancias.append(distancia)
            self.distanciaPromedio()

    def crearPaquete(self):
        self.paquetesEnviados+=1
        recorrido = self.distanciaCorta()
        mensaje = self.vistaPrincipal.mensaje.get()
        rutas = self.calcularRuta(recorrido)
        paquete = pq.Paquete(recorrido[0].corX, recorrido[0].corY, len(self.paquetes), mensaje, recorrido, rutas)
        self.paquetes.append(paquete)
        self.nodos[int(self.vistaPrincipal.nSalida.get())].paquetes.append(paquete)
        #self.panel.graficarPaquete(paquete) 
        self.moverPaquete(paquete,1,0, self.validar)


    def repainPaquete(self):
        if  not self.validar:
            for widget in self.vistaPrincipal.panelDibujo.find_withtag('Paquete'):
                self.vistaPrincipal.panelDibujo.delete(widget)

        for i in self.paquetes:
            self.panel.graficarPaquete(i)
        

    def moverPaquete(self, paquete, i, r, validar):

            self.repainPaquete()
                
            paquete.corX += 1 if paquete.corX < paquete.recorrido[i].corX else -1
            paquete.corY = int(paquete.ruta[r](paquete.corX))

            if(abs(paquete.corY - paquete.recorrido[i].corY) <= 5 and abs(paquete.corX - paquete.recorrido[i].corX)<=5 ):
                if (i+1 < len(paquete.recorrido)):
                    i+=1
                    if r+1 < len(paquete.ruta):
                        r+=1
                else:
                    self.paquetesRecibidos+=1
                    self.paquetes.remove(paquete)
                    return 0
            tiempo = 100 - self.vistaPrincipal.ancho.get() + self.vistaPrincipal.inter.get()  
            self.idFuncionB = self.vistaPrincipal.panelDibujo.after(tiempo, self.moverPaquete, paquete, i, r, validar)

        
    def actualizarDatos(self, tTranscurrido):

        tasaEnvio = round((self.paquetesEnviados/ tTranscurrido)* 60, 2)
        self.vistaPrincipal.tenvio.config(text = tasaEnvio)

        tasaRecibido = round((self.paquetesRecibidos/60) , 2)
        self.vistaPrincipal.trecibido.config(text = tasaRecibido)

        if tasaEnvio > tasaRecibido+2:
            self.vistaPrincipal.ltrafico.config(text = "Medio", bg="yellow")
        elif tasaEnvio > tasaRecibido+4:
            self.vistaPrincipal.ltrafico.config(text = "Alto", bg="red")
        else:
            self.vistaPrincipal.ltrafico.config(text = "Bajo", bg="white")
    

    def distanciaCorta(self):
        dist, nodoInter = 700, 0
        nLlegada = int(self.vistaPrincipal.nLlegada.get())
        nSalida = int(self.vistaPrincipal.nSalida.get())
        recorrido = []
        #Si son nodos contrarios
        if nSalida not in list(self.nodos[nLlegada].distancias.keys()):
            for key, value in self.nodos[nLlegada].distancias.items():
                if value + self.nodos[key].distancias[nSalida] < dist:
                    nodoInter = key
                    dist = value + self.nodos[key].distancias[nSalida]
            recorrido = [self.nodos[nSalida], self.nodos[nodoInter], self.nodos[nLlegada]]
        else:
            recorrido = [self.nodos[nSalida], self.nodos[nLlegada]]

        return recorrido
        
    def calcularRuta(self, nodosCercanos):
        self.paquetesEnviados+=1
        inicio = (nodosCercanos[0].corX, nodosCercanos[0].corY)
        intermedio = (nodosCercanos[1].corX, nodosCercanos[1].corY)

        if len(nodosCercanos)==3:
            llegada = (nodosCercanos[2].corX, nodosCercanos[2].corY)
            recorrido = [inicio, intermedio, llegada]
        else:
            recorrido = [inicio, intermedio]

        rutas = [np.poly1d(np.polyfit([recorrido[0][0], recorrido[1][0]], [recorrido[0][1], recorrido[1][1]], 1))] 
        if(len(recorrido)==3):
            rutas.append(np.poly1d(np.polyfit([recorrido[1][0], recorrido[2][0]], [recorrido[1][1], recorrido[2][1]], 1)))
        
        return rutas

    def distanciaPromedio(self):
        distPromedio = int(sum(self.distancias)/len(self.distancias))
        self.vistaPrincipal.ldist.config(text = distPromedio)
         
    def detenerMovimiento(self):
        self.validar = False
        self.vistaPrincipal.panelDibujo.after_cancel(self.idFuncionA)
        self.tTranscurrido = 0
        self.paquetesEnviados = 0
        
           
    def actualizar(self, idNodo, label):
        for i in self.nodos:
            if i.id == idNodo:
                i.corX = label.winfo_x()
                i.corY = label.winfo_y()
        self.panel.graficarNodo(self.nodos)
        self.crearLineas(self.nodos)

    def delConexiones(self):
        for i in self.nodos:
            i.conexiones = []

    def rePaint(self):
        self.panel.graficarNodo(self.nodos)
        self.crearConexion()
        self.crearLineas(self.nodos)

