from visual import *
from particula import *
from sistemaParticulas import *
from vecinas import *

class Dinamica:

    def LeyDeHook(self, sistemaParticulas, k, h):
        for i in sistemaParticulas.sistemaParticulas:
            fuerzaTotal = vector(0,0,0)
            for j in i.obtenerVecinas():
                distancia = j.getPosicion() - i.getPosicion()
                modulo = sqrt(distancia.x**2 + distancia.y**2 + distancia.z**2)
                
                fuerza = (modulo - h) * (distancia / modulo)
                fuerzaTotal += fuerza
            i.setFuerzaInterna(fuerzaTotal * k)

    def LeyDeHook2(self, particula, k, h):
        fuerzaTotal = vector(0, 0, 0)
        posicion = particula.getPosicion()
        for j in particula.obtenerVecinas():
            posicionJ = j.getPosicion()
            distancia = posicionJ - posicion
            modulo = sqrt(distancia.x**2 + distancia.y**2 + distancia.z**2)

            fuerza = (modulo - h) * (distancia / modulo)
            fuerzaTotal += k * fuerza
        particula.setFuerzaInterna(fuerzaTotal)
        #print(fuerzaTotal)

    def SPH(self, particula, alpha, beta, gamma, k, mu, h):
        vecinas = particula.obtenerVecinas()
        posicion = particula.getPosicion()
        velocidad = particula.getVelocidad()
        
        presion = 0.0
        viscosidad = 0.0

        calculoDensidad(particula, alpha, h)
        
        for j2 in vecinas:
            calculoDensidad(j2, alpha, h)

        densidad = particula.getDensidad()

        for j in vecinas:
            densidadJ = j.getDensidad()
            masaJ = 0.1 #sistema.getMasaParticula()
            posicionJ = j.getPosicion()
            velocidadJ = j.getVelocidad()
            distancia = posicionJ - posicion
            r = sqrt(distancia.x**2 + distancia.y**2 + distancia.z**2)
            
            gradienteKernel = ((beta * 15) / (pi * h**5)) * ((h**2 - r**2)**2)
            laplacianoKernel = ((gamma * 318) / (7 * pi * h**2)) * (h**2 - r**2)
            
            # Gradiente de Presion
            
            presion = ((densidad + densidadJ) / (2 * max(densidad, densidadJ)))
            p = masaJ * presion * gradienteKernel
            fuerzaPresion += p * (-k)
            
            # Fuerza Viscosidad
            '''
            termino1 = velocidad - velocidadJ
            termino2 = sqrt(termino1.x**2 + termino1.y**2 + termino1.z**2)
            v = masaJ * (termino2 / 2) * laplacianoKernel
            viscosidad += mu * v
            '''
            
            termino1 = vector(velocidad.x*distancia.x + velocidad.y*distancia.y + velocidad.z*distancia.z)
            termino2 = vector(velocidadJ.x*distancia.x + velocidadJ.y*distancia.y + velocidadJ.z*distancia.z)
            termino3 = (termino1 / r**2) - (termino2 / r**2)
            termino4 = sqrt(termino3.x**2 + termino3.y**2 + termino3.z**2)
            v = masaJ * termino4 * laplacianoKernel
            viscosidad += mu * v
            
        particula.setPresion(presion)
        particula.setViscosidad(viscosidad)

    def SPH2(self, particula, alpha, beta, gamma, k, mu, h):
        vecinas = particula.obtenerVecinas()
        posicion = particula.getPosicion()
        velocidad = particula.getVelocidad()
        
        presion = 0.0
        viscosidad = 0.0
        densidad = particula.getDensidad()

        for j in vecinas:
            densidadJ = j.getDensidad()
            masaJ = 0.1 #sistema.getMasaParticula()
            posicionJ = j.getPosicion()
            velocidadJ = j.getVelocidad()
            distancia = posicionJ - posicion
            r = sqrt(distancia.x**2 + distancia.y**2 + distancia.z**2)

            
            gradienteKernel = ((beta * 15) / (pi * h**5)) * ((h*h - r*r)**2)
            laplacianoKernel = ((gamma * 318) / (7 * pi * h**2)) * (h**2 - r**2)
            
            # Gradiente de Presion

            if densidad > densidadJ:
                maximo = densidad
            else:
                maximo = densidadJ
            p = masaJ * ((densidad + densidadJ) / (2 * maximo)) * gradienteKernel
            presion += p * (-k)
            
            # Fuerza Viscosidad
            
            termino1 = vector(velocidad.x*distancia.x + velocidad.y*distancia.y + velocidad.z*distancia.z)
            termino2 = vector(velocidadJ.x*distancia.x + velocidadJ.y*distancia.y + velocidadJ.z*distancia.z)
            termino3 = (termino1 / r**2) - (termino2 / r**2)
            termino4 = sqrt(termino3.x**2 + termino3.y**2 + termino3.z**2)
            v = masaJ * termino4 * laplacianoKernel
            viscosidad += mu * v
            
        particula.setPresion(presion)
        particula.setViscosidad(viscosidad)

    def calculoDensidades(self, sistema, alpha, h):
        for i in sistema:
            vecinas = i.obtenerVecinas()
            posicionI = i.getPosicion()
            densidad = 0.0
            for j in vecinas:
                masaJ = 0.1
                posicionJ = j.getPosicion()
                distancia = posicionJ - posicionI
                r = sqrt(distancia.x**2 + distancia.y**2 + distancia.z**2)
                #print("r = " + str(r**2))
                #print("h = " + str(h**2))
            
                kernel = ((alpha * 315) / (64 * pi * h**7)) * ((h**2 - r**2)**3)
        
                densidad += masaJ * kernel
            i.setDensidad(densidad)

def calculoDensidad(particula, alpha, h):
    vecinas = particula.obtenerVecinas()
    posicion = particula.getPosicion()
    velocidad = particula.getVelocidad()
    densidad = 0.0
    for j in particula.obtenerVecinas():
        masaJ = 1
        posicionJ = j.getPosicion()
        velocidadJ = j.getVelocidad()
        distancia = posicionJ - posicion
        r = sqrt(distancia.x**2 + distancia.y**2 + distancia.z**2)
            
        kernel = ((alpha * 315) / (64 * pi * h**7)) * ((h**2 - r**2)**3)
        
        densidad += masaJ * kernel
    particula.setDensidad(densidad)
      
    
