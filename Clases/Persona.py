'''
Created on 12 ene. 2017

@author: Manuel
'''
class Persona(object):
    def __init__(self,nombre,DNI,direccion,telefono,e_mail):
        self.nombre=nombre
        self.DNI=DNI
        self.direccion=direccion
        self.telefono=telefono
        self.e_mail=e_mail
    def mostrar(self):
        print("Nombre: %s"%self.nombre)
        print("DNI: %s"%self.DNI)
        print("Direccion: %s"%self.direccion)
        print("Telefono: %s"%self.telefono)
        if self.e_mail!="":
            print("E-mail: %s"%self.e_mail)

if __name__=="__main__":
    clase=[]
    for x in range(10):
        nombre=input("Ingrese el nombre:")
        DNI=input("Ingrese el DNI:")
        direccion=input("Ingrese la direccion:")
        telefono=input("Ingrese el telefono:")
        e_mail=input("Ingrese el e-mail:")
        clase.append(Persona(nombre,DNI,direccion,telefono,e_mail))
    for i in range(10):
        clase[i].mostrar()