from menu import Menu
from lista import Lista


m = Menu()
l = Lista()


while True:
  m.tipo("principal")
  opc = int(input())
  if opc == 1:
    m.tipo("persona")
  elif opc == 2:
    m.tipo("material")
  elif opc == 3:
    m.tipo("pedido") 
  elif opc == 4:
    m.tipo("devolucion")
  elif opc == 5:
    l.tipo("personas")
  elif opc == 6:
    l.tipo("pedidos")
  elif opc == 7:
    l.tipo("devoluciones")
  elif opc == 8:
    l.tipo("materiales")
  elif opc == 9:
    print("Ha salido del sistema")
    break
