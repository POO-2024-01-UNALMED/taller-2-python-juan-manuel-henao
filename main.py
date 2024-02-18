class Asiento:
    def __init__(self,color=None,precio=None,registro=None):
        self.color=color
        self.precio=precio
        self.registro=registro
    
    def cambiarColor(self,nuevoColor):
        if ((nuevoColor=="rojo")or(nuevoColor=="verde")or(nuevoColor=="amarillo")or(nuevoColor=="negro")or(nuevoColor=="blanco")):
            self.color=nuevoColor

class Motor:
    def __init__(self,numeroCilindros=None,tipo=None,registro=None):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    
    def cambiarRegistro(self,nuevoRegistro):
        self.registro=nuevoRegistro
    
    def asignarTipo(self,nuevoTipo):
        if nuevoTipo=="electrico" or nuevoTipo=="gasolina":
            self.tipo=nuevoTipo

class Auto:
    cantidadCreados=0
    def __init__(self,modelo=None,precio=None,marca=None,registro=None):
        self.modelo=modelo
        self.precio=precio
        self.asientos=[]
        self.marca=marca
        self.motor=Motor()
        self.registro=registro
    
    def cantidadAsientos(self):
        contador=0
        for i in self.asientos:
            if isinstance(i,Asiento):
                contador+=1
        return contador
    
    def verificarIntegridad(self):
        respuesta="Auto original"
        for n in self.asientos:
            if isinstance(n,Asiento):
                if n.registro!=self.registro:
                    respuesta="Las piezas no son originales"
                    break
        if self.registro!=self.motor.registro:
            respuesta="Las piezas no son originales"
        return respuesta

        

        