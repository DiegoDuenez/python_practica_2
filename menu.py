from persona import Persona
from material import Material


m = Material()


class Menu():

  def tipo(self, tipo, p = None):
    if tipo == "principal" and p == None:
      print("- - - MENU PRINCIPAL - - -")
      print("(1) Registrar persona")
      print("(2) Registrar material")
      print("(3) Registrar pedido")
      print("(4) Registrar devolucion")
      print("(5) Lista de personas")
      print("(6) Lista de pedidos")
      print("(7) Lista de devoluciones")
      print("(8) Lista de materiales")
      print("(9) Salir")
      print("          ")

    if tipo == "persona":
      p = Persona()
      print("Ingrese el nombre de la persona:") 
      n = input()
      print("Ingrese la edad de la persona:") 
      e = input()
      p.registrar(n,e)

    if tipo == "material":
      print("Ingrese el nombre del material:") 
      nm = input()
      m.registrar(nm)

    if tipo == "pedido" :
      p = Persona()
      print("Ingrese el ID de la persona:")
      idp = str(input())
      print("Ingrese el ID del material prestado:") 
      idm = str(input())
      print("Ingrese la fecha de pedido (AAAA/MM/DD):")
      fped = input()
      print("          ")
      print("Mensaje: La persona " + str(idp) + " pidió  el material " + str(idm))
      print("          ")
      p.pide(idp, idm, fped)
      
      
    if tipo == "devolucion" :
      p = Persona()
      print("Ingrese el ID de la persona:")
      idp = str(input())
      print("Ingrese el ID del material prestado:") 
      idm = str(input())
      print("Ingrese la fecha de pedido (AAAA/MM/DD):")
      fdev = input()
      print("          ")
      print("Mensaje: La persona " + str(idp) + " devolvio el material " + str(idm))
      print("          ")
      p.devuelve(idp, idm, fdev)
