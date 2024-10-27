from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId
import os

load_dotenv()

class Entity:
    def __init__(self, db_name = os.getenv("DB_NAME"), collection_name = os.getenv("DB_COLLECTION")):
        client = MongoClient(os.getenv("DB_HOST"))
        self.db = client[db_name]
        self.collection = self.db[collection_name]

    def create(self, data):
        return self.collection.insert_one(data)

    def read(self, query = {}):
        entity = self.collection.find_one({"_id": ObjectId(query)})

        entity['_id'] = str(entity['_id'])

        return entity
    
    def read_all(self):
        words = self.collection.find()
        result = []

        for word in words:
            word['_id'] = str(word['_id'])  # Converte ObjectId para string
            result.append(word)

        return result

    def update(self, query, new_values):
        return self.collection.update_one(query, {"$set": new_values})

    def delete(self, query):
        return self.collection.delete_one(query)
