from sqldb import Database 
from archivo import archivo


db = Database()
arc = archivo()


personas = {}
regPed = {}
regDev = {}
regPed['Pedidos'] = []
regDev['Devoluciones'] = []
personas['Personas'] = []


class Persona:
  

  def registrar(self, nombre, edad):
    personas['Personas'] .append({
    'nombre': nombre,
    'edad': edad,
    })
    arc.csv(nombrePer=nombre, edad=edad)
    cl = "personas"
    dic = {"nombre": nombre, "edad":edad}
    db.insert(cl, dic)

  def pide(self, idp, idm, fecha_ped):
    regPed['Pedidos'].append({
    'persona': idp,
    'material': idm,
    'fecha': fecha_ped
    })
    arc.csv(str(idp), str(idm), str(fecha_ped))
    cl = "pedidos"
    dic = {"persona":idp, "material":idm, "fecha": fecha_ped}
    db.insert(cl, dic)
    
  def devuelve(self, idp, idm, fecha_dev):
    regDev['Devoluciones'].append({
      'persona': idp,
      'material': idm,
      'fecha': fecha_dev
    })
    arc.csv(str(idp), str(idm), fecha_dev=str(fecha_dev))
    cl = "devoluciones"
    dic = {"persona":idp, "material":idm, "fecha": fecha_dev}
    cl2 = "pedidos"
    dic2 = { "persona": idp, "material":idm }
    db.insert(cl, dic)
    db.delete(cl2, dic2)
    
  
    

  
      
      

  

 


