from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List, Optional
import requests
import os
import shutil
from pymongo import MongoClient

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIRECTORY = "./uploads"
EXTERNAL_API_URL = "http://10.33.9.30:8000/video/upload"

client = MongoClient("mongodb://localhost:27017/")
db = client["OIM"]
collection = db["analysis"]

os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

@app.post("/upload/")
async def upload_videos(
    files: List[UploadFile] = File(...),
    bedNumbers: List[str] = Form(...),
    collectionDates: List[str] = Form(...),
    gpsFiles: Optional[List[UploadFile]] = None,
):
    try:
        for idx, file in enumerate(files):
            analysis = {}

            file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
            with open(file_path, "wb") as f:
                shutil.copyfileobj(file.file, f)

            with open(file_path, "rb") as f:
                response = requests.post(
                    EXTERNAL_API_URL,
                    files={"file": f},
                )
            
            response_data = response.json()
            unique_id = response_data.get("unique_id")
            print(response_data)

            response = requests.post(f"http://10.33.9.30:5000/{unique_id}")
            print(response)

            bed_number = bedNumbers[idx]
            collection_date = collectionDates[idx]

            analysis['video_id'] = unique_id
            analysis['bed_number'] = bed_number
            analysis['collection_date'] = collection_date
            analysis['analysis'] = response.json()

            collection.insert_one(analysis)
            os.remove(file_path)

        return JSONResponse(content={"message": "success"}, status_code=200, media_type="application/json")

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)