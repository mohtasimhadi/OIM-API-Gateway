from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["OIM"]
collection = db["analysis"]

def insert_analysis(analysis: dict):
    """Insert analysis record into the MongoDB collection."""
    collection.insert_one(analysis)

def get_analysis_by_video_id(video_id: str) -> dict:
    """Retrieve analysis data for the given video ID from MongoDB."""
    analysis_data = collection.find_one({"video_id": video_id})
    if analysis_data:
        analysis_data["_id"] = str(analysis_data["_id"])
        return analysis_data
    return None

def get_all_analysis_summaries() -> list:
    """Retrieve summaries of all analyses from MongoDB."""
    summaries = []
    try:
        print("Attempting to connect to MongoDB...")
        cursor = collection.find({}, {"video_id": 1, "bed_number": 1, "collection_date": 1})
        for document in cursor:
            summaries.append({
                "video_id": document.get("video_id"),
                "bed_number": document.get("bed_number"),
                "collection_date": document.get("collection_date"),
            })
        print("Summaries fetched from MongoDB:", summaries)
    except Exception as e:
        print("Error while fetching summaries:", e)
    return summaries

