from visual import *
from particula import *
from sistemaParticulas import *
from math import * 

def calculaVecinas(sistemaParticulas, separacion):
    for i in sistemaParticulas.sistemaParticulas:
        i.listaVecinas = []
        moduloI = sqrt(i.getPosicion().x**2 + i.getPosicion().y**2 + i.getPosicion().z**2)
        listaJ = sistemaParticulas.sistemaParticulas
        for j in listaJ:
            if i != j:
                moduloJ = sqrt(j.getPosicion().x**2 + j.getPosicion().y**2 + j.getPosicion().z**2)
                distancia = abs(moduloJ - moduloI)
                if distancia <= separacion:
                    i.anadirVecina(j)

def calculaVecinas2(particula, sistemaParticulas, h):
    posicion = particula.getPosicion()
    for j in sistemaParticulas:
        if particula != j:
            posicionJ = j.getPosicion()
            distancia = posicionJ - posicion
            modulo = sqrt(distancia.x**2 + distancia.y**2 + distancia.z**2)
            if modulo <= h:
                particula.anadirVecina(j)
