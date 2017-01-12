'''
Created on 12 ene. 2017

@author: usuario
'''
import math
class Punto(object):
    def __init__(self,origenx,origeny,coordenadax,coordenaday):
        self.origenx=origenx
        self.origeny=origeny
        self.coordenadax=coordenadax
        self.coordenaday=coordenaday
    def distancia(self):
        return math.sqrt(self.coordenadax**2+self.coordenaday**2)
    def muestra_punto(self):
        print(self.coordenadax,self.coordenaday)