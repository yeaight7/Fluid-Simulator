from visual import *
from particula import *

# Gestor de Colisiones

def gestorColisionesLimites(limitesCaja, limitesCubo, posicionEsfera, radioEsfera, posicionCilindro, radioCilindro, axis, espesor, particula):
    LimitesCajaX = (limitesCaja[0], limitesCaja[1])
    LimitesCajaY = (limitesCaja[2], limitesCaja[3])
    LimitesCajaZ = (limitesCaja[4], limitesCaja[5])

    LimitesCuboX = (limitesCubo[0], limitesCubo[1])
    LimitesCuboY = (limitesCubo[2], limitesCubo[3])
    LimitesCuboZ = (limitesCubo[4], limitesCubo[5])
    
    colisionContenedor = detectaColisionLimite(LimitesCajaX, LimitesCajaY, LimitesCajaZ, espesor, particula)
    colisionCubo = detectaColisionCubo(LimitesCuboX, LimitesCuboY, LimitesCuboZ, espesor, particula)
    colisionEsfera = detectaColisionEsfera(posicionEsfera, radioEsfera, espesor, particula)
    colisionCilindro = detectaColisionCilindro(posicionCilindro, radioCilindro, axis, espesor, particula)

    if colisionContenedor[0] == True or colisionCubo[0] == True or colisionEsfera[0] == True or colisionCilindro[0] == True:
        vectorNormal = colisionContenedor[1] + colisionCubo[1] + colisionEsfera[1] + colisionCilindro[1]
        respuestaColisionLimites(particula, vectorNormal, espesor)

    colisiones = (colisionContenedor[0], colisionCubo[0], colisionEsfera[0], colisionCilindro[0])
    return colisiones

# Deteccion de las Colisiones

def detectaColisionLimite(LimitesX, LimitesY, LimitesZ, espesor, particula):
    posicion = particula.getPosicion()
    velocidad = particula.getVelocidad()

    LimX_inf = LimitesX[0] + espesor
    LimX_sup = LimitesX[1] - espesor
    LimY_inf = LimitesY[0] + espesor
    LimY_sup = LimitesY[1] - espesor
    LimZ_inf = LimitesZ[0] + espesor
    LimZ_sup = LimitesZ[1] - espesor

    vectorNormal = vector(0.0, 0.0, 0.0)
    colision = False

    if posicion.x < LimX_inf or posicion.x > LimX_sup or posicion.y < LimY_inf or posicion.y > LimY_sup or posicion.z < LimZ_inf or posicion.z > LimZ_sup:        
        if posicion.x < LimX_inf:
            vectorNormal += vector(1.0, 0.0, 0.0)
        elif posicion.x > LimX_sup:
            vectorNormal += vector(-1.0, 0.0, 0.0)
        if posicion.y < LimY_inf:
            vectorNormal += vector(0.0, 1.0, 0.0)
        elif posicion.y > LimY_sup:
            vectorNormal += vector(0.0, -1.0, 0.0)
        if posicion.z < LimZ_inf:
            vectorNormal += vector(0.0, 0.0, 1.0)
        elif posicion.z > LimZ_sup:
            vectorNormal += vector(0.0, 0.0, -1.0)
        colision = True
            
    colisiona = (colision, vectorNormal)
    return colisiona

def detectaColisionCubo(LimitesX, LimitesY, LimitesZ, espesor, particula):
    posicion = particula.getPosicion()
    velocidad = particula.getVelocidad()

    LimX_inf = LimitesX[0] - espesor
    LimX_sup = LimitesX[1] + espesor
    LimY_inf = LimitesY[0] - espesor
    LimY_sup = LimitesY[1] + espesor
    LimZ_inf = LimitesZ[0] - espesor
    LimZ_sup = LimitesZ[1] + espesor

    vectorNormal = vector(0.0, 0.0, 0.0)
    colision = False

    if posicion.x > LimX_inf and posicion.x < LimX_sup and posicion.y > LimY_inf and posicion.y < LimY_sup and posicion.z > LimZ_inf and posicion.z < LimZ_sup:
        modulo = sqrt(velocidad.x*velocidad.x + velocidad.y*velocidad.y + velocidad.z*velocidad.z)
        normal = velocidad / modulo

        sueloX = LimitesX[0]
        techoX = LimitesX[1]
        sueloY = LimitesY[0]
        techoY = LimitesY[1]
        sueloZ = LimitesZ[0]
        techoZ = LimitesZ[1]

        if posicion.x < sueloX:
            vectorNormal += vector(-abs(normal.x), 0.0, 0.0)
        elif posicion.x > techoX:
            vectorNormal += vector(abs(normal.x), 0.0, 0.0)
        if posicion.y < sueloY:
            vectorNormal += vector(0.0, -abs(normal.y), 0.0)
        elif posicion.y > techoY:
            vectorNormal += vector(0.0, abs(normal.y), 0.0)
        if posicion.z < sueloZ:
            vectorNormal += vector(0.0, 0.0, -abs(normal.z))
        elif posicion.z > techoZ:
            vectorNormal += vector(0.0, 0.0, abs(normal.z))
        colision = True

    colisiona = (colision, vectorNormal)
    return colisiona
    
def detectaColisionEsfera(posicionEsfera, radioEsfera, espesor, particula):
    posicionParticula = particula.getPosicion()

    limite = radioEsfera + espesor
    
    distancia = posicionParticula - posicionEsfera
    moduloDist = sqrt(distancia.x*distancia.x + distancia.y*distancia.y + distancia.z*distancia.z)
    
    vectorNormal = vector(0.0,0.0,0.0)
    colision = False
    
    if moduloDist < limite:
        colision = True
        vectorNormal = vectorNormal + distancia / moduloDist

    colisiona = (colision, vectorNormal)
    return colisiona
    
def detectaColisionCilindro(posicionCilindro, radioCilindro, axis, espesor, particula):
    posicion = particula.getPosicion()
    velocidad = particula.getVelocidad()

    vectorNormal = vector(0.0, 0.0, 0.0)
    colision = False
    
    if axis.x == 1.0:
        longitud = axis.x
        limiteRadio = radioCilindro + espesor

        modulo = sqrt(velocidad.x*velocidad.x + velocidad.y*velocidad.y + velocidad.z*velocidad.z)
        normal = velocidad / modulo

        distancia = vector(0.0, posicion.y - posicionCilindro.y, posicion.z - posicionCilindro.z)
        moduloDist = sqrt(distancia.y*distancia.y + distancia.z*distancia.z)
        
        cilindroTecho = posicionCilindro + vector(longitud, 0.0, 0.0)
        limiteSup = cilindroTecho.x + espesor
        cilindroSuelo = posicionCilindro
        limiteInf = cilindroSuelo.x - espesor

        if moduloDist < limiteRadio:
            if posicion.x < limiteSup and posicion.x > cilindroTecho.x:
                colision = True
                vectorNormal += vector(abs(normal.x), 0.0, 0.0)
            if posicion.x > limiteInf and posicion.x < cilindroSuelo.x:
                colision = True
                vectorNormal += vector(-abs(normal.x), 0.0, 0.0)
            if posicion.x < cilindroTecho.x and posicion.x > cilindroSuelo.x:
                colision = True
                vectorNormal += distancia / moduloDist
    
    elif axis.y == 1.0:
        longitud = axis.y
        limiteRadio = radioCilindro + espesor

        modulo = sqrt(velocidad.x*velocidad.x + velocidad.y*velocidad.y + velocidad.z*velocidad.z)
        normal = velocidad / modulo

        distancia = vector(posicion.x - posicionCilindro.x, 0.0, posicion.z - posicionCilindro.z)
        moduloDist = sqrt(distancia.x*distancia.x + distancia.z*distancia.z)
        
        cilindroTecho = posicionCilindro + vector(0.0, longitud, 0.0)
        limiteSup = cilindroTecho.y + espesor
        cilindroSuelo = posicionCilindro
        limiteInf = cilindroSuelo.y - espesor

        if moduloDist < limiteRadio:
            if posicion.y < limiteSup and posicion.y > cilindroTecho.y:
                colision = True
                vectorNormal += vector(0.0, abs(normal.y), 0.0)
            if posicion.y > limiteInf and posicion.y < cilindroSuelo.y:
                colision = True
                vectorNormal += vector(0.0, -abs(normal.y), 0.0)
            if posicion.y < cilindroTecho.y and posicion.y > cilindroSuelo.y:
                colision = True
                vectorNormal += distancia / moduloDist
                
    elif axis.z == 1.0 or axis.z > 1.0:
        longitud = axis.z
        limiteRadio = radioCilindro + espesor

        modulo = sqrt(velocidad.x*velocidad.x + velocidad.y*velocidad.y + velocidad.z*velocidad.z)
        normal = velocidad / modulo

        distancia = vector(posicion.x - posicionCilindro.x, posicion.y - posicionCilindro.y, 0.0)
        moduloDist = sqrt(distancia.x*distancia.x + distancia.y*distancia.y)
        
        cilindroTecho = posicionCilindro + vector(0.0, 0.0, longitud)
        limiteSup = cilindroTecho.z + espesor
        cilindroSuelo = posicionCilindro
        limiteInf = cilindroSuelo.z - espesor

        if moduloDist < limiteRadio:
            if posicion.z < limiteSup and posicion.z > cilindroTecho.z:
                colision = True
                vectorNormal += vector(0.0, 0.0, abs(normal.z))
            if posicion.z > limiteInf and posicion.z < cilindroSuelo.z:
                colision = True
                vectorNormal += vector(0.0, 0.0, -abs(normal.z))
            if posicion.z < cilindroTecho.z and posicion.z > cilindroSuelo.z:
                colision = True
                vectorNormal += distancia / moduloDist
                
    colisiona = (colision, vectorNormal)
    return colisiona

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

# Respuestas a las Colisiones

def respuestaColisionLimites(particula, vectorNormal, espesor):
    tasaRozamiento = 0.95
    tasaRebote = 0.35
    tasaEspesor = 0.005
    
    velocidad = particula.getVelocidad()
    posicion = particula.getPosicion()
    
    velEscalar = velocidad.x * vectorNormal.x + velocidad.y * vectorNormal.y + velocidad.z * vectorNormal.z
    
    velocidadNormal = vector(vectorNormal.x * velEscalar, vectorNormal.y * velEscalar , vectorNormal.z * velEscalar)
    velocidadTangencial = velocidad - velocidadNormal

    # Amortiguamiento
    
    terminoAngular = sqrt(2.0  / 3.0) * pi
    terminoCreador = tasaRebote * terminoAngular
    terminoAtenuador = 7.84616
    tauRebote = terminoCreador / terminoAtenuador
    normal = sqrt(velocidadNormal.x*velocidadNormal.x + velocidadNormal.y*velocidadNormal.y + velocidadNormal.z*velocidadNormal.z)
    modNormal = tauRebote * normal
    
    velocidadRebote = vector(velocidadNormal.x * modNormal, velocidadNormal.y * modNormal, velocidadNormal.z * modNormal)
    #velocidadRebote = vector(velocidadNormal.x * tasaRebote, -velocidadNormal.y * tasaRebote, velocidadNormal.z * tasaRebote)
    velocidadRozamiento = vector(velocidadTangencial.x * tasaRozamiento, velocidadTangencial.y * tasaRozamiento, velocidadTangencial.z * tasaRozamiento)
    
    velocidadFinal = velocidadRebote + velocidadRozamiento
    particula.setVelocidad(velocidadFinal)
    
    posicionFinal = posicion + vectorNormal * tasaEspesor
    particula.setPosicion(posicionFinal)
