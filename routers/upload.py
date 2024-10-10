from fastapi import APIRouter, File, UploadFile, Form
from fastapi.responses import JSONResponse
from typing import List, Optional
from utils import db_utils, file_utils, external_api

router = APIRouter()

@router.post("/")
async def upload_videos(
    files: List[UploadFile] = File(...),
    bedNumbers: List[str] = Form(...),
    collectionDates: List[str] = Form(...),
    gpsFiles: Optional[List[UploadFile]] = None,
):
    try:
        for idx, file in enumerate(files):
            file_path = file_utils.save_upload_file(file)
            response_data = external_api.upload_video(file_path)
            unique_id = response_data.get("unique_id")

            analysis_result = external_api.request_analysis(unique_id)

            analysis = {
                'video_id': unique_id,
                'bed_number': bedNumbers[idx],
                'collection_date': collectionDates[idx],
                'plants': set([data['class_name'] for data in analysis['track_data']]),
                'analysis': analysis_result,
            }
            db_utils.insert_analysis(analysis)

            file_utils.remove_file(file_path)

        return JSONResponse(content={"message": "success"}, status_code=200, media_type="application/json")

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)