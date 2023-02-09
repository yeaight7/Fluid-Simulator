from visual import *
from particula import *
from sistemaParticulas import *
from vecinas import *

class Dinamicas:

    def LeyDeHook(self, sistemaParticulas, k, h):
        for i in sistemaParticulas.sistemaParticulas:
            fuerzaTotal = vector(0.0, 0.0, 0.0)
            vecinas = i.obtenerVecinas()
            for j in vecinas:
                distancia = j.getPosicion() - i.getPosicion()
                modulo = sqrt(distancia.x*distancia.x + distancia.y*distancia.y + distancia.z*distancia.z)
                if modulo < h:
                    fuerza = (modulo - h) * (distancia / modulo)
                    fuerzaTotal += fuerza
            i.setFuerzaInterna(fuerzaTotal * k)

    def LeyDeHookParticula(self, particula, k, h):
        posicion = particula.getPosicion()
        vecinas = particula.obtenerVecinas()

        fuerzaTotal = vector(0.0, 0.0, 0.0)
        for j in vecinas:
            posicionJ = j.getPosicion()

            distancia = posicionJ - posicion
            modulo = sqrt(distancia.x*distancia.x + distancia.y*distancia.y + distancia.z*distancia.z)

            fuerza = (modulo - h) * (distancia / modulo)
            fuerzaTotal += fuerza
        particula.setFuerzaInterna(fuerzaTotal * k)

    def SPH(self, sistema, alpha, beta, gamma, k, mu, h):
        for i in sistema:
            posicionI = i.getPosicion()
            velocidadI = i.getVelocidad()
            vecinas = i.obtenerVecinas()
            densidadI = i.getDensidad()
            
            presion = 0.0
            fuerzaPresion = vector(0.0, 0.0, 0.0)

            viscosidad = 0.0
            fuerzaViscosidad = vector(0.0 ,0.0, 0.0)

            for j in vecinas:
                posicionJ = j.getPosicion()
                velocidadJ = j.getVelocidad()
                densidadJ = j.getDensidad()
                masaJ = j.getMasa()

                distancia = posicionJ - posicionI
                r = sqrt(distancia.x*distancia.x + distancia.y*distancia.y + distancia.z*distancia.z)

                if r < h:
                    gradienteKernel = (((beta * 15) / (pi * h**5)) * ((h*h - r*r)**2)) * (distancia / r)
                    laplacianoKernel = ((gamma * 318) / (7 * pi * h*h)) * (h*h - r*r)

                    # Presion y Fuerza de Presion

                    if densidadI > densidadJ:
                        maximo = densidadI
                    elif densidadJ >= densidadI:
                        maximo = densidadJ

                    p = (densidadI + densidadJ) / (2 * maximo)
                    presion += p
                    fuerzaP = p * gradienteKernel * (-k) * masaJ
                    fuerzaPresion += fuerzaP

                    # FuerzaViscosidad

                    termino1 = vector(velocidadI.x*distancia.x, velocidadI.y*distancia.y, velocidadI.z*distancia.z)
                    termino2 = vector(velocidadJ.x*distancia.x, velocidadJ.y*distancia.y, velocidadJ.z*distancia.z)
                    termino3 = (termino1 / (r * r)) - (termino2 / (r * r))
                    v = sqrt(termino3.x*termino3.x + termino3.y*termino3.y + termino3.z*termino3.z)
                    fuerzaV = termino3 * laplacianoKernel * (-mu) * masaJ
                    fuerzaViscosidad += fuerzaV

            i.setPresion(presion)
            i.setFuerzaPresion(fuerzaPresion)
            i.setFuerzaViscosidad(fuerzaViscosidad)
                    

    def SPHParticula(self, particula, alpha, beta, gamma, k, mu, h):
        posicionI = particula.getPosicion()
        velocidadI = particula.getVelocidad()
        vecinas = particula.obtenerVecinas()

        densidadI = particula.getDensidad()

        presion = 0.0
        fuerzaPresion = vector(0.0, 0.0, 0.0)

        viscosidad = 0.0
        fuerzaViscosidad = vector(0.0, 0.0, 0.0)

        for j in vecinas:
            posicionJ = j.getPosicion()
            velocidadJ = j.getVelocidad()
            densidadJ = j.getDensidad()
            masaJ = j.getMasa()

            distancia = posicionJ - posicionI
            r = sqrt(distancia.x*distancia.x  + distancia.y*distancia.y + distancia.z*distancia.z)

            gradienteKernel = (((beta * 15) / (pi * h**5)) * ((h*h - r*r)**2)) * (distancia / r)
            laplacianoKernel = ((gamma * 318) / (7 * pi * h*h)) * (h*h - r*r)

            # Presion y Fuerza de Presion

            if densidadI > densidadJ:
                maximo = densidadI
            else:
                maximo = densidadJ
            p = (densidadI + densidadJ) / (2 * maximo)
            presion += p
            fuerzaPresion += masaJ * p * gradienteKernel * (-k)

            # Viscosidad y FuerzaViscosidad

            termino1 = vector(velocidadI.x*distancia.x, velocidadI.y*distancia.y, velocidadI.z*distancia.z)
            termino2 = vector(velocidadJ.x*distancia.x, velocidadJ.y*distancia.y, velocidadJ.z*distancia.z)
            termino3 = (termino1 / (r*r)) - (termino2 / (r*r))
            v = sqrt(termino3.x*termino3.x + termino3.y*termino3.y + termino3.z*termino3.z)
            viscosidad += v
            fuerzaViscosidad += (-mu * masaJ * laplacianoKernel) * termino3

        particula.setPresion(presion)
        particula.setFuerzaPresion(fuerzaPresion)

        particula.setViscosidad(viscosidad)
        particula.setFuerzaViscosidad(fuerzaViscosidad)

    def calculoDensidades(self, sistema, alpha, h):
        for i in sistema:
            posicionI = i.getPosicion()
            vecinas = i.obtenerVecinas()
            densidad = 0.0
            for j in vecinas:
                posicionJ = j.getPosicion()
                masaJ = 0.1

                distancia = posicionJ - posicionI
                r = sqrt(distancia.x*distancia.x + distancia.y*distancia.y + distancia.z*distancia.z)

                kernel = ((alpha * 315) / (64 * pi * h**7)) * ((h*h - r*r)**3)

                densidad += masaJ * kernel
            i.setDensidad(densidad)
