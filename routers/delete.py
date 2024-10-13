from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils import db_utils, external_api

router = APIRouter()

@router.get("/{video_id}")
async def delete_analysis(video_id: str):
    analysis_data = db_utils.get_analysis_by_video_id(video_id)
    if analysis_data:
        db_utils.delete_analysis(video_id)
        response = external_api.delete_video(analysis_data['video_id'])
        if response['detail'] == 'Video deleted successfully':
            print("Deleted original video.")
        else:
            return JSONResponse(content={"success": False}, status_code=404)
        if response['detail'] == 'Video deleted successfully':
            print("Deleted annotated video.")
        else:
            return JSONResponse(content={"success": False}, status_code=404)
        print(response)
        for i, track_data in enumerate(analysis_data['analysis']['track_data']):
            response = external_api.delete_image(track_data['image'])
            print(f"Deleted {i+1}/{len(analysis_data['analysis']['track_data'])} tracked images.")
        
        return JSONResponse(content={"success": True}, status_code=200)
    return JSONResponse(content={"success": False}, status_code=404)