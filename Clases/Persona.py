'''
Created on 12 ene. 2017

@author: usuario
'''
class Persona(object):
    def __init__(self,nombre,DNI,direccion,telefono,e_mail):
        self.nombre=nombre
        self.DNI=DNI
        self.direccion=direccion
        self.telefono=telefono
        self.e_mail=e_mail
    def mostrar(self):
        print(self.nombre)
        print(self.DNI)
        print(self.direccion)
        print(self.telefono)
        if self.e_mail!="":
            print(self.e_mail)