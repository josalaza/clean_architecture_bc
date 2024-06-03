from pymongo import MongoClient
from base_datos import BaseDatos

class MongoDB(BaseDatos):
    def __init__(self, uri, database, collection):

        self.client = MongoClient(uri)
        self.db = self.client[database]
        self.collection = self.db[collection]

    def guardar(self, datos):
        if self.collection:
            self.collection.insert_one({"contenido": datos})
        else:
            print("No se pudo conectar")

    def leer(self):
        if self.collection:
            return [doc["contenido"] for doc in self.collection.find()]
        else:
            print("No se pudo conectar")
            return []
