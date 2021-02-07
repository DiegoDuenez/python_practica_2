import mysql.connector as mysql


mydb = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="python_practica"
    )
print(mydb)


mycursor = mydb.cursor()


class Database:

    def all(self):
        mycursor.execute("SHOW DATABASES")
        for x in mycursor:
            print(x)
    
    def insert(self, tab, cond):
        if tab == "personas":
            x = cond.get('nombre')
            y = cond.get('edad')
            mycursor.execute('INSERT INTO personas (nombre, edad) values ("%s", "%s")' % (x, y))
            mydb.commit()
        elif tab == "materiales":
            x = cond.get('nombre')
            mycursor.execute('INSERT INTO materiales (nombre) values ("%s")' % (x))
            mydb.commit()
        elif tab == "pedidos" or tab == "devoluciones":
            x = cond.get('persona')
            y = cond.get('material')
            z = cond.get('fecha')
            mycursor.execute('INSERT INTO %s (persona, material, fecha) values ("%s","%s","%s")' % (tab, x, y, z))
            mydb.commit()
        else:
            print("La tabla %s no se encuentra en el sistema" % (tab))           
    
    def select(self, tab):
        mycursor.execute('SELECT * FROM %s' % (tab))
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

    def delete(self, tab, cond):
        if tab == "persona":
            x = cond.get('nombre')
            mycursor.execute('DELETE FROM persona where nombre = "%s"' % (x))
            mydb.commit()
        elif tab == "materiales":
            x = cond.get('nombre')
            mycursor.execute('DELETE FROM materiales where nombre = "%s"' % (x))
            mydb.commit()
        elif tab == "pedidos" or tab == "devoluciones":
            x = cond.get('persona')
            y = cond.get('material')
            mycursor.execute('DELETE FROM %s where persona = "%s" and material = "%s"' % (tab, x, y))
            mydb.commit()
        else:
            print("La tabla %s no se encuentra en el sistema" % (tab))           
        


        
    
   



        
        