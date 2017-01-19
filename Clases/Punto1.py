'''
Created on 12 ene. 2017

@author: Manuel
'''
import math
class Punto(object):
    origenx=0
    origeny=0
    def __init__(self,coordenadax,coordenaday):
        self.coordenadax=coordenadax
        self.coordenaday=coordenaday
    def distancia(self):
        return math.sqrt(self.coordenadax**2+self.coordenaday**2)
    def muestra_punto(self):
        print(self.coordenadax,self.coordenaday)

punto1=Punto(0,0)
punto2=Punto(0,0)
punto1_coordenadax=int(input("Escriba la coordenada x del primer punto:"))
setattr(punto1,"coordenadax",punto1_coordenadax)
punto1_coordenaday=int(input("Escriba la coordenada y del primer punto:"))
setattr(punto1,"coordenaday",punto1_coordenaday)
punto2_coordenadax=int(input("Escriba la coordenada x del primer punto:"))
setattr(punto2,"coordenadax",punto2_coordenadax)
punto2_coordenaday=int(input("Escriba la coordenada y del primer punto:"))
setattr(punto2,"coordenaday",punto2_coordenaday)

if punto1.distancia()>punto2.distancia():
    punto2.muestra_punto()
else:
    punto1.muestra_punto()