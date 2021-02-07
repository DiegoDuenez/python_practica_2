import csv


tb = "pedidos"


class archivo:

    def csv(self, idp = None, idm = None, fecha_ped = None, nombreMat = None, fecha_dev = None, nombrePer = None, edad = None):
        if idp and idm and fecha_ped:
            archivo = open("datos/Pedidos.csv", "a")
            archivo.write(idp)
            archivo.write(",")
            archivo.write(idm)
            archivo.write(",")
            archivo.write(fecha_ped)
            archivo.write("\n")
            archivo.close()
        elif nombreMat:
            archivo = open("datos/Materiales.csv", "a")
            archivo.write(nombreMat)
            archivo.write("\n")
            archivo.close()
        elif idp and idm and fecha_dev:
            archivo = open("datos/Devoluciones.csv", "a")
            archivo.write(idp)
            archivo.write(",")
            archivo.write(idm)
            archivo.write(",")
            archivo.write(fecha_dev)
            archivo.write("\n")
            archivo.close()
        elif nombrePer and edad:
            archivo = open("datos/Personas.csv", "a")
            archivo.write(nombrePer)
            archivo.write(",")
            archivo.write(edad)
            archivo.write("\n")
            archivo.close()

            