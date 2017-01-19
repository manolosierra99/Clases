

'''
Created on 11 ene. 2017

@author: Manuel
'''
class Cuenta(object):
    def __init__(self,saldo):
        self.saldo=saldo
    def ingresar(self,cantidad1):
        self.saldo=self.saldo+cantidad1
    def retirar(self,cantidad2):
        if cantidad2>self.saldo:
            print("Lo siento, no tienes ese dinero en la cuenta.")
        else:
            self.saldo=self.saldo-cantidad2

cuenta1=Cuenta(0.0)
cuenta1.ingresar(125.23)
print(getattr(cuenta1,"saldo"))
cuenta1.ingresar(503.4)
print(getattr(cuenta1,"saldo"))
cuenta1.ingresar(50)
print(getattr(cuenta1,"saldo"))
cuenta1.retirar(333.34)
print(getattr(cuenta1,"saldo"))