from visual import *
from particula import *
from sistemaParticulas import *

def generaColumna(posicionInicial, masa, numParticulasX, numParticulasY, numParticulasZ, separacion, velocidadInicial, radio):
    
    xInicial = posicionInicial.x
    yInicial = posicionInicial.y
    zInicial = posicionInicial.z
    
    fuenteColumna = SistemaParticulas()

    # Calculo de los angulos de giro de la columna
    
    moduloVel = sqrt(velocidadInicial.x**2 + velocidadInicial.y**2 + velocidadInicial.z**2)
    if moduloVel != 0:
        aux = velocidadInicial / moduloVel
    else:
        aux = vector(0.0, -1.0, 0.0)
    
    alpha = acos(aux.y)
    if velocidadInicial.x < 0:
        alpha = alpha * -1
    beta = asin(aux.z / sin(alpha))
    
    for i in range(numParticulasX):                 # Bucle para la fila en X
        i += 1
        for j in range(numParticulasY):             # Bucle para la columna en Y
            j += 1
            for z in range(numParticulasZ):         # Bucle para la altura en Z
                posicionFinal = vector(xInicial, yInicial, zInicial)

                # Calculo de la posicion con la inclinacion
                
                auxY = calculoVectorMatriz(posicionFinal, "y", alpha)
                posicionFinal = auxY
                auxZ = calculoVectorMatriz(posicionFinal, "z", beta)
                posicionFinal = auxZ 
                
                particulaGenerada = Particula(posicionFinal, velocidadInicial, radio)
                fuenteColumna.agregaParticula(particulaGenerada)
                zInicial += separacion
                z += 1
            yInicial += separacion
            zInicial = posicionInicial.z
        xInicial += separacion
        yInicial = posicionInicial.y

    return fuenteColumna

def generaColumnaCilindrica(posicionInicial, masa, numParticulasY, numAros, separacion, velocidadInicial, radio):

    xInicial = posicionInicial.x
    yInicial = posicionInicial.y
    zInicial = posicionInicial.z
    
    fuenteColumna = SistemaParticulas()
    
    # Calculo de los angulos de giro de la columna
    
    moduloVel = sqrt(velocidadInicial.x**2 + velocidadInicial.y**2 + velocidadInicial.z**2)
    if moduloVel != 0:
        aux = velocidadInicial / moduloVel
    else:
        aux = vector(0.0, -1.0, 0.0)
    
    alpha = acos(aux.y)
    if velocidadInicial.x < 0:
        alpha = alpha * -1
    beta = asin(aux.z / sin(alpha))
    
    for i in range(numParticulasY):                         # Bucle para la altura de la columna cilindrica
        i += 1
        longitud = separacion
        for j in range(numAros):                            # Bucle para el nivel del anillo
            if j == 0:                                      # Columna principal
                
                # Calculo de la posicion con la inclinacion
                
                posicionFinal = vector(xInicial, yInicial, zInicial)

                # Calculo de la posicion con la inclinacion de la columna principal
                 
                auxY = calculoVectorMatriz(posicionFinal, "y", alpha)
                posicionFinal = auxY
                auxZ = calculoVectorMatriz(posicionFinal, "z", beta)
                posicionFinal = auxZ
                
                particulaGenerada = Particula(posicionFinal, velocidadInicial, radio)
                fuenteColumna.agregaParticula(particulaGenerada)
            else:
                cantidadVuelta = j * 4                                  # Particulas por anillo, multiplo de 4
                anguloDiv = (2 * pi) / cantidadVuelta
                angulo = 0# + (anguloDiv * i) / 5                       # Rotacion si fuese la columna entera
                for k in range(cantidadVuelta):                         # Bucle para las particulas de cada anillo
                    posicionX = xInicial + cos(angulo) * longitud
                    posicionZ = zInicial + sin(angulo) * longitud
                    
                    # Calculo de la posicion con la inclinacion
                    
                    posicionFinal = vector(posicionX, yInicial, posicionZ)

                    auxY = calculoVectorMatriz(posicionFinal, "y", alpha)
                    posicionFinal = auxY
                    auxZ = calculoVectorMatriz(posicionFinal, "z", beta)
                    posicionFinal = auxZ
                    
                    particulaGenerada = Particula(posicionFinal, velocidadInicial, radio)
                    fuenteColumna.agregaParticula(particulaGenerada)
                    angulo += anguloDiv
                longitud += separacion
            j+= 1
        xInicial = posicionInicial.x
        zInicial = posicionInicial.z
        yInicial += separacion

    return fuenteColumna


def generaColumnaEsfera(posicionInicial, masa, arosDiametro, separacion, velocidadInicial, radio):

    xInicial = posicionInicial.x
    yInicial = posicionInicial.y
    zInicial = posicionInicial.z
    
    fuenteColumna = SistemaParticulas()

    giros = arosDiametro
    posicionActual = vector(xInicial, yInicial, zInicial)

    rot = 0
    aux = int(pi / (pi/6))

    for i in range(aux):
        i += 1
        longitud = separacion
        posicionActual = vector(xInicial, yInicial, zInicial)
        for j in range(int(giros)):
            if j != 0:
                cantidadVuelta = j * 4
                anguloDiv = (2 * pi) / cantidadVuelta
                angulo = 0
                for k in range(cantidadVuelta):
                    posicionX = xInicial + cos(angulo) * longitud
                    posicionZ = zInicial + sin(angulo) * longitud
                    posicionActual = vector(posicionX, yInicial, posicionZ)
                    posicionActual = calculoVectorMatriz(posicionActual, "y", rot)
                    posicionActual = calculoVectorMatriz(posicionActual, "x", pi/2)
                    
                    particulaGenerada = Particula(posicionActual, velocidadInicial, radio)
                    fuenteColumna.agregaParticula(particulaGenerada)
                    
                    angulo += anguloDiv
                longitud += separacion
            j += 1
        rot += pi/6
        xInicial = posicionInicial.x
        zInicial = posicionInicial.z
        
    return fuenteColumna

def generaColumnaEspiral(posicionInicial, masa, arosDiametro, altura, separacion, velocidadInicial, radio, momento):
    
    xInicial = posicionInicial.x
    yInicial = posicionInicial.y
    zInicial = posicionInicial.z
    
    fuenteColumna = SistemaParticulas()
    rot = 0

    # Calculo de los angulos de giro de la columna
    
    moduloVel = sqrt(velocidadInicial.x**2 + velocidadInicial.y**2 + velocidadInicial.z**2)
    if moduloVel != 0:
        aux = velocidadInicial / moduloVel
    else:
        aux = vector(0.0, -1.0, 0.0)
    
    alpha = acos(aux.y)
    if velocidadInicial.x < 0:
        alpha = alpha * -1
    beta = asin(aux.z / sin(alpha))
    beta = pi + beta
    alpha = pi - alpha
    
    for i in range(altura):
        longitud = separacion
        cantidadAro = 2
        for j in range(arosDiametro):
            if j > 1:
                angulo = 0
                for k in range(cantidadAro):
                    largo = longitud / cantidadAro
                    
                    posicionX = xInicial + cos(angulo) * longitud
                    posicionY = yInicial
                    posicionZ = zInicial + sin(angulo) * longitud

                    posicionFinal = vector(posicionX, posicionY, posicionZ)
                    posicionFinal = calculoVectorMatriz(posicionFinal, "z", momento+rot)

                    # Calculo de la posicion con la inclinacion
                    
                    posicionFinal = calculoVectorMatriz(posicionFinal, "y", alpha)
                    posicionFinal = calculoVectorMatriz(posicionFinal, "z", beta)

                    particulaGenerada = Particula(posicionFinal, velocidadInicial, radio)
                    fuenteColumna.agregaParticula(particulaGenerada)

                    angulo += ((pi / 4) / cantidadAro)
                    k += 1

            longitud += separacion
            j += 1
            if j % 2 == 0:
                cantidadAro += 1
        i += 1
        xInicial += posicionInicial.x
        yInicial += separacion
        zInicial += posicionInicial.z
        rot += pi / 10

    return fuenteColumna

def generaColumnaCono(posicionInicial, masa, arosDiametro, altura, separacion, velocidadInicial, radio):

    xInicial = posicionInicial.x
    yInicial = posicionInicial.y
    zInicial = posicionInicial.z
    
    fuenteColumna = SistemaParticulas()

    # Calculo de los angulos de giro de la columna
    
    moduloVel = sqrt(velocidadInicial.x**2 + velocidadInicial.y**2 + velocidadInicial.z**2)
    if moduloVel != 0:
        aux = velocidadInicial / moduloVel
    else:
        aux = vector(0.0, -1.0, 0.0)
    
    alpha = acos(aux.y)
    if velocidadInicial.x < 0:
        alpha = alpha * -1
    beta = asin(aux.z / sin(alpha))
    beta = pi + beta
    alpha = pi - alpha
    
    for i in range(altura):
        longitud = separacion
        aros = i + 1
        for j in range(aros):
            if j == 0:
                posicionFinal = vector(xInicial, yInicial, zInicial)

                # Calculo de la posicion con la inclinacion
                    
                posicionFinal = calculoVectorMatriz(posicionFinal, "y", alpha)
                posicionFinal = calculoVectorMatriz(posicionFinal, "z", beta)
                
                particulaGenerada = Particula(posicionFinal, velocidadInicial, radio)
                fuenteColumna.agregaParticula(particulaGenerada)
            else:
                cantidadVuelta = j * 6
                anguloDiv = (2 * pi) / cantidadVuelta
                angulo = 0

                for k in range(cantidadVuelta):
                    posicionX = xInicial + cos(angulo) * longitud
                    posicionY = yInicial
                    posicionZ = zInicial + sin(angulo) * longitud

                    posicionFinal = vector(posicionX, posicionY, posicionZ)

                    # Calculo de la posicion con la inclinacion
                    
                    posicionFinal = calculoVectorMatriz(posicionFinal, "y", alpha)
                    posicionFinal = calculoVectorMatriz(posicionFinal, "z", beta)
                
                    particulaGenerada = Particula(posicionFinal, velocidadInicial, radio)
                    fuenteColumna.agregaParticula(particulaGenerada)

                    angulo += anguloDiv
            longitud += separacion
            j += 1
        xInicial = posicionInicial.x
        yInicial += separacion
        zInicial = posicionInicial.z
        i += 1

    return fuenteColumna


def calculoVectorMatriz(vect, transformada, angulo):
    if transformada == "x":
        matriz1 = vector(1, 0, 0)
        matriz2 = vector(0, cos(angulo), -sin(angulo))
        matriz3 = vector(0, sin(angulo), cos(angulo))
        
        posicion = vector(vect.x, vect.y*matriz2.y+vect.z*matriz3.y, vect.y*matriz2.z+vect.z*matriz3.z)
        
    if transformada == "y":
        matriz1 = vector(cos(angulo), -sin(angulo), 0)
        matriz2 = vector(sin(angulo), cos(angulo), 0)
        matriz3 = vector(0, 0, 1)
        
        posicion = vector(vect.x*matriz1.x+vect.y*matriz2.x, vect.x*matriz1.y+vect.y*matriz2.y, vect.z)        
        
    if transformada == "z":
        matriz1 = vector(cos(angulo), 0, sin(angulo))
        matriz2 = vector(0, 1, 0)
        matriz3 = vector(-sin(angulo), 0, cos(angulo))
        
        posicion = vector(vect.x*matriz1.x+vect.z*matriz3.x, vect.y, vect.x*matriz1.z+vect.z*matriz3.z)        
        
    return posicion
