
class Controlador:
    def __init__(self, logica, vista):
        self.logica = logica
        self.vista = vista

    def realizarOp(self, accion):
        if(accion=="agregar"):
            self.logica.agregarNodo()
        elif(accion=="eliminar"):
            self.logica.eliminarNodo()
        elif(accion == "aleatoriamente"):
            self.logica.moverAleatorio()
        elif(accion == "enviar"):
            self.logica.crearPaquete()
        elif(accion == "detener"):
            self.logica.detenerMovimiento()
            
    def soltarEti(self, event):
        id = event.widget.cget("text")
        self.logica.actualizar(id, event.widget)

    def arrastrarEti(self, event):
        self.logica.moverNodo(event.x, event.y, event.widget)
        
        