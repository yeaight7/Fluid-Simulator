from visual import *
from particula import *
'''
def gestorMultiplesColisiones(LimitesX, LimitesY, LimitesZ, espesor, particula, posicionEsfera, radioEsfera):
    vectorNormal = vector(0.0, 0.0, 0.0)

    colisionContenedor = detectaColisionLimite(LimitesX, LimitesY, LimitesZ, espesor, particula, vectorNormal)
    vectorNormal = colisionContenedor[1]
    colisionEsfera = detectaColisionEsfera(posicionEsfera, radioEsfera, espesor, particula, vectorNormal)
    vectorNormal = colisionEsfera[1]

    a = False
    b = vectorNormal
    
    if colisionContenedor[0] == True or colisionEsfera[0] == True:
        respuestaColisionLimites(particula, vectorNormal, espesor)
        print("Vector Normal: " + str(vectorNormal))
        a = True
        
    fin = (a,b)
    return fin
'''
def detectaColisionLimite(LimitesX, LimitesY, LimitesZ, espesor, particula):
    posicion = particula.getPosicion()
    velocidad = particula.getVelocidad()

    LimX_inf = LimitesX[0] + espesor
    LimX_sup = LimitesX[1] - espesor
    LimY_inf = LimitesY[0] + espesor
    LimY_sup = LimitesY[1] - espesor
    LimZ_inf = LimitesZ[0] + espesor
    LimZ_sup = LimitesZ[1] - espesor
    
    #vectorNormal = vectorNor
    #colisiona = (False, vectorNormal)
    
    colisiona = (False," ")

    if posicion.x < LimX_inf or posicion.x > LimX_sup or posicion.y < LimY_inf or posicion.y > LimY_sup or posicion.z < LimZ_inf or posicion.z > LimZ_sup:

        if posicion.x < LimX_inf:
            #vectorNormal += vector(1.0, 0.0, 0.0)
            colisiona = (True,"x")
            respuestaColision(particula, "x")
        if posicion.x > LimX_sup:
            #vectorNormal += vector(-1.0, 0.0, 0.0)
            colisiona = (True,"-x")
            respuestaColision(particula, "-x")
        if posicion.y < LimY_inf:
            #vectorNormal += vector(0.0, 1.0, 0.0)
            colisiona = (True,"y")
            respuestaColision(particula, "y")
        if posicion.y > LimY_sup:
            #vectorNormal += vector(0.0, -1.0, 0.0)
            colisiona = (True,"-y")
            respuestaColision(particula, "-y")
        if posicion.z < LimZ_inf:
            #vectorNormal += vector(0.0, 0.0, 1.0)
            colisiona = (True,"z")
            respuestaColision(particula, "z")
        if posicion.z > LimZ_sup:
            #vectorNormal += vector(0.0, 0.0, -1.0)
            colisiona = (True,"-z")
            respuestaColision(particula, "-z")

        #colisiona = (True, vectorNormal)

    return colisiona


def detectaColisionLimites(LimitesX, LimitesY, LimitesZ, espesor, particula):
    posicion = particula.getPosicion()
    velocidad = particula.getVelocidad()

    LimX_inf = LimitesX[0] + espesor
    LimX_sup = LimitesX[1] - espesor
    LimY_inf = LimitesY[0] + espesor
    LimY_sup = LimitesY[1] - espesor
    LimZ_inf = LimitesZ[0] + espesor
    LimZ_sup = LimitesZ[1] - espesor

    #normal_x = vector(velocidad.x,0.0,0.0)
    #normal_y = vector(0.0,velocidad.y,0.0)
    #normal_z = vector(0.0,0.0,velocidad.z)

    normal_x = vector(1.0,0.0,0.0)
    normal_y = vector(0.0,1.0,0.0)
    normal_z = vector(0.0,0.0,1.0)

    vectorNormal = vector(0.0, 0.0, 0.0)
     
    colisiona = (False," ")

    if posicion.x < LimX_inf or posicion.x > LimX_sup:

        if posicion.x < LimX_inf:
            colisiona = (True,"x")
            vectorNormal += normal_x
        else:
            colisiona = (True,"-x")
            normal_x = normal_x * -1
            vectorNormal += normal_x

        
    if posicion.y < LimY_inf:
        colisiona = (True,"y")
        vectorNormal += normal_y

    
    if posicion.z < LimZ_inf or posicion.z > LimZ_sup:
        
        if posicion.z < LimZ_inf:
            colisiona = (True,"z")
            vectorNormal += normal_z
        else:
            colisiona = (True,"-z")
            normal_z = normal_z * -1
            vectorNormal += normal_z

    
    if colisiona[0] == True:
        #moduloVector = sqrt(vectorNormal.x**2 + vectorNormal.y**2 + vectorNormal.z**2)
        #vectorNormal = vectorNormal / moduloVector
		
        respuestaColisionLimites(particula,vectorNormal,espesor)
    return colisiona


def respuestaColision(particula, vectorNormal):
    tasaRozamiento = 0.95
    tasaRebote = 0.5
    tasaEspesor = 0.005

    posicion = particula.getPosicion()
    velocidad = particula.getVelocidad()

    if vectorNormal == "x":
        posicionFinal = vector(posicion.x + tasaEspesor, posicion.y, posicion.z)
        #velocidadRoz = abs(velocidad.x) * tasaRozamiento
        velocidadRoz = vector(0.0, velocidad.y * tasaRozamiento, velocidad.z * tasaRozamiento)
        velocidadReb = abs(velocidad.x) * tasaRebote
        #velocidadFinal = vector(abs(velocidad.x) - velocidadRoz - velocidadReb, velocidad.y, velocidad.z)
        velocidadFinal = vector(velocidadReb, 0.0, 0.0) + velocidadRoz
    if vectorNormal == "-x":
        posicionFinal = vector(posicion.x - tasaEspesor, posicion.y, posicion.z)
        #velocidadRoz = abs(velocidad.x) * tasaRozamiento
        velocidadRoz = vector(0.0, velocidad.y * tasaRozamiento, velocidad.z * tasaRozamiento)
        velocidadReb = abs(velocidad.x) * tasaRebote
        #velocidadFinal = vector(-abs(velocidad.x) + velocidadRoz + velocidadReb, velocidad.y, velocidad.z)
        velocidadFinal = vector(-velocidadReb, 0.0, 0.0) + velocidadRoz
        
    if vectorNormal == "y":
        posicionFinal = vector(posicion.x, posicion.y + tasaEspesor, posicion.z)
        #velocidadRoz = abs(velocidad.y) * tasaRozamiento
        velocidadRoz = vector(velocidad.x * tasaRozamiento, 0.0, velocidad.z * tasaRozamiento)
        velocidadReb = abs(velocidad.y) * tasaRebote
        #velocidadFinal = vector(velocidad.x, abs(velocidad.y) - velocidadRoz - velocidadReb, velocidad.z)
        velocidadFinal = vector(0.0, velocidadReb, 0.0) + velocidadRoz
    if vectorNormal == "-y":
        posicionFinal = vector(posicion.x, posicion.y - tasaEspesor, posicion.z)
        #velocidadRoz = abs(velocidad.y) * tasaRozamiento
        velocidadRoz = vector(velocidad.x * tasaRozamiento, 0.0, velocidad.z * tasaRozamiento)
        velocidadReb = abs(velocidad.y) * tasaRebote
        #velocidadFinal = vector(velocidad.x, -abs(velocidad.y) + velocidadRoz + velocidadReb, velocidad.z)
        velocidadFinal = vector(0.0, -velocidadReb, 0.0) + velocidadRoz
        
    if vectorNormal == "z":
        posicionFinal = vector(posicion.x, posicion.y, posicion.z + tasaEspesor)
        #velocidadRoz = abs(velocidad.z) * tasaRozamiento
        velocidadRoz = vector(velocidad.x * tasaRozamiento, velocidad.y * tasaRozamiento, 0.0)
        velocidadReb = abs(velocidad.z) * tasaRebote
        #velocidadFinal = vector(velocidad.x, velocidad.y, abs(velocidad.z) - velocidadRoz - velocidadReb)
        velocidadFinal = vector(0.0, 0.0, velocidadReb) + velocidadRoz
    if vectorNormal == "-z":
        posicionFinal = vector(posicion.x, posicion.y, posicion.z - tasaEspesor)
        #velocidadRoz = abs(velocidad.z) * tasaRozamiento
        velocidadRoz = vector(velocidad.x * tasaRozamiento, velocidad.y * tasaRozamiento, 0.0)
        velocidadReb = abs(velocidad.z) * tasaRebote
        #velocidadFinal = vector(velocidad.x, velocidad.y, -abs(velocidad.z) + velocidadRoz + velocidadReb)
        velocidadFinal = vector(0.0, 0.0, -velocidadReb) + velocidadRoz

    particula.setPosicion(posicionFinal)
    particula.setVelocidad(velocidadFinal)

def detectaColisionDistancias(limite1, limite2, limite3, particula):
    posicion = particula.getPosicion()
    
    r12 = limite2 - limite1
    r13 = limite3 - limite1
    superficie = vector(r12.y*r13.z - r12.z*r13.y, r12.z*r13.x - r12.x*r13.z, r12.x*r13.y - r12.y*r13.x)
    superficieEscalar = sqrt(superficie.x**2 + superficie.y**2 + superficie.z**2)
    
    r0p = posicion - limite1
    volumen = vector(r0p.x * superficie.x, r0p.y * superficie.y, r0p.z * superficie.z)
    volumenEscalar = sqrt(volumen.x**2 + volumen.y**2 + volumen.z**2)
    
    altura = volumenEscalar / superficieEscalar

    proyeccionX = (posicion.x + (altura / superficieEscalar)) * superficie.x
    proyeccionY = (posicion.y + (altura / superficieEscalar)) * superficie.y
    proyeccionZ = (posicion.z + (altura / superficieEscalar)) * superficie.z
    
    proyeccion  = vector(proyeccionX, proyeccionY, proyeccionZ)
    
    proyeccion0 = vector(proyeccion.x * limite1.x, proyeccion.y * limite1.y, proyeccion.z * limite1.z)
    proyeccion1 = vector(proyeccion.x * limite2.x, proyeccion.y * limite2.y, proyeccion.z * limite2.z)
    proyeccion2 = vector(proyeccion.x * limite3.x, proyeccion.y * limite3.y, proyeccion.z * limite3.z)

    moduloP0 = sqrt(proyeccion0.x**2 + proyeccion0.y**2 + proyeccion0.z**2)
    moduloP1 = sqrt(proyeccion1.x**2 + proyeccion1.y**2 + proyeccion1.z**2)
    moduloP2 = sqrt(proyeccion2.x**2 + proyeccion2.y**2 + proyeccion2.z**2)
    
    angulo1 = acos((proyeccion0.x*proyeccion1.x + proyeccion0.y*proyeccion1.y + proyeccion0.z*proyeccion1.z)/ (moduloP0 * moduloP1))
    angulo2 = acos((proyeccion1.x*proyeccion2.x + proyeccion1.y*proyeccion2.y + proyeccion1.z*proyeccion2.z)/ (moduloP1 * moduloP2))
    angulo3 = acos((proyeccion2.x*proyeccion0.x + proyeccion2.y*proyeccion0.y +  proyeccion2.z*proyeccion0.z)/ (moduloP2 * moduloP0))

    anguloTotal = angulo1 + angulo2 + angulo3

    colision = []
    if anguloTotal == 2 * pi:
        colision.append(True)
        colision.append("y")
        return colision

def detectaColisionEsfera(posicionEsfera, radioEsfera, espesor, particula):
    posicionParticula = particula.getPosicion()
    
    distancia = posicionParticula - posicionEsfera
    moduloDist  = sqrt(distancia.x**2 + distancia.y**2 + distancia.z**2)
    
    limite = radioEsfera + espesor
    vectorNormal = vector(0.0,0.0,0.0)
    #colisiona = (False, vectorNor)
    
    if moduloDist < limite:
        vectorNormal = vectorNormal + distancia / moduloDist
        respuestaColisionLimites(particula, vectorNormal, espesor)
        #colisiona = (True, vectorNormal)
        return True
    return False
    #return colisiona
        
def respuestaColisionLimites(particula, vectorNormal, espesor):
    tasaRozamiento = 0.95
    tasaRebote = 0.5
    tasaEspesor = 0.05
    
    velocidad = particula.getVelocidad()
    posicion = particula.getPosicion()
    
    velEscalar = velocidad.x * vectorNormal.x + velocidad.y * vectorNormal.y + velocidad.z * vectorNormal.z
    
    velocidadNormal = vector(vectorNormal.x * velEscalar, vectorNormal.y * velEscalar , vectorNormal.z * velEscalar)
    velocidadTangencial = velocidad - velocidadNormal
    
    velocidadRebote = vector(velocidadNormal.x * tasaRebote, velocidadNormal.y * tasaRebote, velocidadNormal.z * tasaRebote)
    velocidadRozamiento = vector(velocidadTangencial.x * tasaRozamiento, velocidadTangencial.y * tasaRozamiento, velocidadTangencial.z * tasaRozamiento)
    
    velocidadFinal = velocidadRebote + velocidadRozamiento
    particula.setVelocidad(velocidadFinal)
    
    posicionFinal = posicion + vectorNormal * tasaEspesor
    particula.setPosicion(posicionFinal)
