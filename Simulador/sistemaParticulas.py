from visual import *    # from mathutils import *
from particula import *

class SistemaParticulas:

    def __init__(self):
        self.sistemaParticulas = []
        self.radioParticula = 0.0
          
    #--------------------------------
    #         Consultores
    #--------------------------------
    
    def getParticula(self,indice):
        return self.sistemaParticulas[indice]
    
    def getIndiceParticula(self, particula):
        return self.sistemaParticulas.index(particula)
      
    def getNumeroParticulas(self):
        return len(self.sistemaParticulas)

    def getParticulas(self):
        return self.sistemaParticulas

    #--------------------------------
    #         Modificadores
    #--------------------------------

    def agregaParticula(self,particula):
        self.sistemaParticulas.append(particula)
        
    def agregaParticulaIndex(self, particula, indice):
        self.sistemaParticulas.insert(indice, particula)
        
    def eliminaParticula(self,particula):
        self.sistemaParticulas.remove(particula)
        
    def eliminaParticulaPorIndice(self,indice):
        self.sistemaParticulas.pop(indice)
    
    def permutaParticula(self, indicePermutacion, particula):
        self.sistemaParticulas.pop(indicePermutacion)
        self.sistemaParticulas.insert(indicePermutacion,particula)

    def setSistemaParticulas(self, nuevoSistemaParticulas):
        self.sistemaParticulas = nuevoSistemaParticulas

    def agregaSistemaParticulas(self, nuevoSistemaParticulas):
        for i in nuevoSistemaParticulas.getParticulas():
            self.agregaParticula(i)
