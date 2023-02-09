from visual import *

def MetodoEuler(particula, aceleracion, pasoTiempo):
    posicion = particula.getPosicion()
    velocidad = particula.getVelocidad()
    masa = particula.getMasa()

    fuerzaTotal = particula.getFuerzaTotal()
    '''
    fuerzaInterna = particula.getFuerzaInterna()
    fuerzaPresion = particula.getFuerzaPresion()
    fuerzaViscosidad = particula.getFuerzaViscosidad()
    
    print("Fuerza Interna -> " + str(fuerzaInterna.x) + " , " + str(fuerzaInterna.y) + " , " + str(fuerzaInterna.z))
    print("Fuerza Presion -> " + str(fuerzaPresion.x) + " , " + str(fuerzaPresion.y) + " , " + str(fuerzaPresion.z))
    print("Fuerza Viscosida -> " + str(fuerzaViscosidad.x) + " , " + str(fuerzaViscosidad.y) + " , " + str(fuerzaViscosidad.z))
    print("-------------------------------------------------")
    '''
    fuerzas = fuerzaTotal / masa
    aceleraciones = aceleracion + fuerzas
    
    posicionFinal = posicion + velocidad * pasoTiempo + (aceleraciones * (pasoTiempo**2)) / 2
    velocidadFinal = velocidad + aceleracion * pasoTiempo

    salida = [posicionFinal, velocidadFinal]
    return salida

