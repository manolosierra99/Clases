

'''
Created on 11 ene. 2017

@author: usuario
'''
import math
class Cuenta(object):
    saldo=0.0
    def ingresar(self,cantidad1):
        self.saldo=self.saldo+cantidad1
    def retirar(self,cantidad2):
        if cantidad2>self.saldo:
            print("Lo siento, no tienes ese dinero en la cuenta.")
        else:
            self.saldo=self.saldo-cantidad2
class Persona(object):
    nombre=""
    DNI=""
    direccion=""
    telefono=""
    e_mail=""
    def mostrar(self):
        print(self.nombre)
        print(self.DNI)
        print(self.direccion)
        print(self.telefono)
        if self.e_mail!="":
            print(self.e_mail)
class Punto(object):
    origenx=0
    origeny=0
    coordenadax=""
    coordenaday=""
    def distancia(self):
        return math.sqrt(self.coordenadax**2+self.coordenaday**2)
    def muestra_punto(self):
        print(self.coordenadax,self.coordenaday)
