from sqldb import Database
from archivo import archivo


db = Database()
arc = archivo()


mat = {}
mat['Materiales'] = []


class Material:

  def registrar(self,nombre):

    mat['Materiales'].append({
    'nombre': nombre,
    })
    arc.csv(nombreMat = nombre)
    cl = "materiales"
    dic = {"nombre":nombre}
    db.insert(cl, dic)
    
  
    

    
