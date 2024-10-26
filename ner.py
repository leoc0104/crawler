import spacy
from pymongo import MongoClient

nlp = spacy.load("en_core_web_sm")

client = MongoClient("mongodb://localhost:27017/")
db = client["fatec"]
collection = db["entities"]

def process_and_store_entities(text):
    doc = nlp(text)
    entities = []

    for ent in doc.ents:
        entities.append({
            "text": ent.text,
            "label": ent.label_
        })

    if entities:
        collection.insert_many(entities)
        print("Entities saved to MongoDB")

with open("output.txt", "r") as file:
    text = file.read()

process_and_store_entities(text)
