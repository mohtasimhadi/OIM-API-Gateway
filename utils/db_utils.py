from pymongo import MongoClient
from utils.config import Config

client = MongoClient(Config.MONGODB_URI)
db = client["OIM"]
collection = db["analysis"]

def insert_analysis(analysis: dict):
    collection.insert_one(analysis)

def delete_analysis(video_id: str):
    collection.delete_one({'video_id': video_id})

def get_analysis_by_video_id(video_id: str) -> dict:
    analysis_data = collection.find_one({"video_id": video_id})
    if analysis_data:
        analysis_data["_id"] = str(analysis_data["_id"])
        return analysis_data
    return None

def get_all_analysis_summaries() -> list:
    summaries = []
    try:
        cursor = collection.find({}, {"video_id": 1, "bed_number": 1, "collection_date": 1, "plants": 1})
        for document in cursor:
            summaries.append({
                "video_id": document.get("video_id"),
                "bed_number": document.get("bed_number"),
                "collection_date": document.get("collection_date"),
                "plants": document.get("plants")
            })
    except Exception as e:
        print("Error while fetching summaries:", e)
    return summaries

