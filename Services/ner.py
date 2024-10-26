import spacy
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

nlp = spacy.load("en_core_web_sm")

client = MongoClient(os.getenv("DB_HOST"))
db = client[os.getenv("DB_NAME")]
collection = db[os.getenv("DB_COLLECTION")]

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
