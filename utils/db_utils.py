from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["OIM"]
collection = db["analysis"]

def insert_analysis(analysis: dict):
    """Insert analysis record into the MongoDB collection."""
    collection.insert_one(analysis)