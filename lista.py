from sqldb import Database 


db = Database()


class Lista:

    def tipo(self, tipo):
        if tipo == "pedidos":
            print("- - - LISTA DE PERSONAS QUE PIDIERON - - -")
            print("ID | PERSONA | MATERIAL | FECHA")
            tb = "pedidos"
            db.select(tb)
            print("- - - - - - - - - - - - - - - - - - - - - - -")
        elif tipo == "devoluciones":  
            print("- - - LISTA DE PERSONAS QUE DEVOLVIERON - - -")
            print("ID | PERSONA | MATERIAL | FECHA")
            tb = "devoluciones"
            db.select(tb)
            print("- - - - - - - - - - - - - - - - - - - - - - -")
        elif tipo == "personas":
            print("- - - LISTA DE PERSONAS - - -")
            print("ID | PERSONA | EDAD")
            tb = "personas"
            db.select(tb)
            print("- - - - - - - - - - - -  - - -")
        elif tipo == "materiales":
            print("- - - LISTA DE MATERIALES - - - - - - - - - -")
            print("ID | NOMBRE")
            tb = "materiales"
            db.select(tb)
            print("- - - - - - - - - - - - - - - - - - - - - - -")
        else:
            print("El tipo de lista %s no se encuentra" % (tipo))


   