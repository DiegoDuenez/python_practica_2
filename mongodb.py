import pymongo
import dns


client = pymongo.MongoClient("mongodb+srv://diego:192712883@cluster0.o7i7b.mongodb.net/python_practica?retryWrites=true&w=majority")
db = client.python_practica


#print(client.list_database_names())
#print("   ")
#print(db.list_collection_names())


class Database():
    
    def all(self):
        print(client.list_database_names())
        
    def insert(self, col, dic):
        col = db[col]
        col.insert_one(dic)
        
    def select(self, tabla):
        col = db[tabla]
        for dato in col.find():
            print(dato)
    
    def delete(self, col, dic):
        col = db[col]
        col.delete_one(dic)



        

                

