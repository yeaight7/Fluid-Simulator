from visual import *

class Particula:

    def __init__(self, posicion, velocidad, radio):
        self.body = sphere(pos = posicion, radius = radio)
        self.velocity = velocidad
        self.body.color = color.blue
        
        self.listaVecinas = []
        self.fuerzaInterna = vector(0.0, 0.0, 0.0)

        self.masa = 0.1

        self.densidad = 0.0
        
        self.presion = 0.0
        self.fuerzaPresion = vector(0.0, 0.0, 0.0)
        
        self.viscosidad = 0.0
        self.fuerzaViscosidad = vector(0.0, 0.0, 0.0)

        self.fuerzaTotal = vector(0.0, 0.0, 0.0)

    # -------------------
    # Metodos Consultores
    # -------------------

    def getPosicion(self):
        return self.body.pos

    def getVelocidad(self):
        return self.velocity

    def getColor(self):
        return self.body.color

    def getRadio(self):
        return self.body.radius

    def getMasa(self):
        return self.masa

    # ---------------------
    # Metodos Modificadores
    # ---------------------

    def setPosicion(self, posicion):
        self.body.pos = posicion

    def setVelocidad(self, velocidad):
        self.velocity = velocidad

    def setColor(self, colorDado):
        self.body.color = colorDado

    def setRadio(self, radio):
        self.body.radius = radio

    def setMasa(self, m):
        self.masa = m

    # -------
    # Vecinas
    # -------
    
    def anadirVecina(self, particula):
        self.listaVecinas.append(particula)
    
    def obtenerVecinas(self):
        return self.listaVecinas

    def getNumeroVecinas(self):
        return len(self.listaVecinas)

    def setListaVecinas(self, listaV):
        self.listaVecinas = listaV

    # --------------
    # Fuerza Vecinas
    # --------------
    
    def getFuerzaInterna(self):
        return self.fuerzaInterna

    def setFuerzaInterna(self, fuerza):
        self.fuerzaInterna = fuerza

    # ---------------
    # SPH Consultores
    # ---------------

    def getDensidad(self):
        return self.densidad

    def getPresion(self):
        return self.presion

    def getFuerzaPresion(self):
        return self.fuerzaPresion

    def getViscosidad(self):
        return self.viscosidad

    def getFuerzaViscosidad(self):
        return self.fuerzaViscosidad

    def getFuerzaTotal(self):
        return self.fuerzaTotal

    # -----------------
    # SPH Modificadores
    # -----------------

    def setDensidad(self, d):
        self.densidad = d

    def setPresion(self, p):
        self.presion = p

    def setFuerzaPresion(self, fuerzaP):
        self.fuerzaPresion = fuerzaP

    def setViscosidad(self, v):
        self.viscosidad = v

    def setFuerzaViscosidad(self, fuerzaV):
        self.fuerzaViscosidad = fuerzaV

    def setFuerzaTotal(self, fuerzaT):
        self.fuerzaTotal = fuerzaT

