from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils import db_utils

router = APIRouter()

@router.get("/summaries")
async def get_analysis_summaries():
    print("This is redirecting to summaries")
    summaries = db_utils.get_all_analysis_summaries()
    print("Summaries fetched:", summaries)
    return JSONResponse(content=summaries, status_code=200, media_type="application/json")

@router.get("/{video_id}")
async def get_analysis(video_id: str):
    """Retrieve the analysis data for a given video ID."""
    analysis_data = db_utils.get_analysis_by_video_id(video_id)
    if not analysis_data:
        raise JSONResponse(content={"message": "Analysis not found"}, status_code=404, detail="Analysis not found")
    return JSONResponse(content=analysis_data, status_code=200, media_type="application/json")