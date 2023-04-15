import sys

from vista import vista as v

from modelo import Logic as lg

from controlador import Controller as c

vistaPrincipal = v.vista()

logica = lg.Logica(vistaPrincipal)

control = c.Controlador(logica, vistaPrincipal)

vistaPrincipal.actualizarControl(control)

vistaPrincipal.ventana.mainloop()
