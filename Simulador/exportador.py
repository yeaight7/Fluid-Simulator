from visual import *
from struct import *


def exportar(Archivo, nFrame, sistemaParticulas, radioParticula):
        
	numParticulas = len(sistemaParticulas)
	name = Archivo + str(nFrame).zfill(5) +'.bin'
	archivo = open(name,'wb')
	crearCabecera(archivo, nFrame, numParticulas, radioParticula)
	
	for i in range(numParticulas):
                particula_i = sistemaParticulas[i]
                posicion_i = particula_i.getPosicion()
                velocidad_i = particula_i.getVelocidad()
                fuerza_i = particula_i.getFuerzaInterna()
                vecinas_i = particula_i.getNumeroVecinas()

                densidad_i = particula_i.getDensidad()
                presion_i = particula_i.getPresion()
                viscosidad_i = particula_i.getViscosidad()
                
                posX = posicion_i.x
                posY = posicion_i.y
                posZ = posicion_i.z

                velocidadX = velocidad_i.x
                velocidadY = velocidad_i.y
                velocidadZ = velocidad_i.z

                modulo = sqrt(velocidadX*velocidadX + velocidadY*velocidadY + velocidadZ*velocidadZ)
                normal = vector(velocidadX / modulo, velocidadY / modulo, velocidadZ / modulo)
                normalX = normal.x
                normalY = normal.y
                normalZ = normal.z

                fuerzaX = fuerza_i.x
                fuerzaY = fuerza_i.y
                fuerzaZ = fuerza_i.z
                
                
                #[float]*3 ; particle position (XYZ-global)
                archivo.write(pack('fff', posX, posY, posZ))
                
                #[float]*3 ; particle velocity (XYZ)
                archivo.write(pack('fff', velocidadX, velocidadY, velocidadZ))
                
                #[float]*3 ; particle force (XYZ)
                archivo.write(pack('fff', fuerzaX, fuerzaY, fuerzaZ))
                
                #[float]*3 ; particle vorticity (XYZ) ;; version>=9
                archivo.write(pack('fff', 0.0, 0.0, 0.0))
                
                #[float]*3 ; normal vector (XYZ) ;; version>=3                
                archivo.write(pack('fff', normalX, normalY, normalZ))
                
                #[int] ; number of neighbors ;; version>=4
                archivo.write(pack('i', vecinas_i))
                
                #[float]*3 ; Texture vector (UVW) ;; version>=5
                archivo.write(pack('fff', 0.0, 0.0, 0.0))
                
                #[short int] ; info bits ;; version>=5
                archivo.write(pack('h', 0))
                
                #[float] ; elapsed particle time (age)
                archivo.write(pack('f', 0.0))
                
                #[float] ; isolation time
                archivo.write(pack('f', 0.0))
                
                #[float] ; viscosity
                archivo.write(pack('f', viscosidad_i))
                
                #[float] ; density
                archivo.write(pack('f', densidad_i))
                
                #[float] ; pressure
                archivo.write(pack('f', presion_i))
                
                #[float] ; mass
                archivo.write(pack('f', 0.1))
                
                #[float] ; temperature
                archivo.write(pack('f', 0.0))
                
                #[uint64] ; particle ID ;; version>=12
                archivo.write(pack('I', 0))
                
        ###Cadena final####
                
        #un cero entero
	archivo.write(pack('i', 0))
	
	#un caracter 00 en hexadecimal
	archivo.write(pack('c', b'\x00'))
	
	#un caracter 00 en hexadecimal
	archivo.write(pack('c', b'\x00'))
	
	#cerrar archivo
	archivo.close()
	

def crearCabecera(archivo, nFrame, numParticulas, radioParticula):

        nombreCabecera = 'ExportadorRealFlow'
        archivo.write(pack('i',int('0xFABADA',0)))
        
        talla1 = len(nombreCabecera)
        talla2 = 250 - talla1
        archivo.write(nombreCabecera.encode())

        
        for i in range(1, talla2+1):
            #un caracter 00 en hexadecimal
            archivo.write(pack('c', b'\x00'))
        #[short int] ; Version Realflow valido 9
        archivo.write(pack('h', 9))
        #[float] ; scale scene
        archivo.write(pack('f', 1.0))
        #[int] ; fluid type p.e. 9
        archivo.write(pack('i', 9))
        #[float] ; elapsed simulation time
        archivo.write(pack('f', 0.0))
        #[int] ; frame number
        archivo.write(pack('i', nFrame))
        #[int] ; frames per second p.e.30
        archivo.write(pack('i', 30))
        #[long int] ; number of particles
        archivo.write(pack('l', numParticulas))
        #[float] ; radius
        archivo.write(pack('f', radioParticula))
        #[float]*3 ; pressure (max, min, average)
        archivo.write(pack('fff', 0.0, 0.0, 0.0))
        #[float]*3 ; speed (max, min, average)
        archivo.write(pack('fff', 0.0, 0.0, 0.0))
        #[float]*3 ; temperature (max, min, average)
        archivo.write(pack('fff', 0.0, 0.0, 0.0))
        #[float]*3 ; emitter position ;; version>=7
        archivo.write(pack('fff', 0.0, 0.0, 0.0))
        #[float]*3 ; emitter rotation ;; version>=7
        archivo.write(pack('fff', 0.0, 0.0, 0.0))
        #[float]*3 ; emitter scale ;; version>=7
        archivo.write(pack('fff', 1.0, 1.0, 1.0))

