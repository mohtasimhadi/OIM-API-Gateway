from fastapi import APIRouter, Response, Request
from fastapi.responses import FileResponse
import httpx
from utils.config import Config
from utils.file_utils import create_xlsx
import tempfile

router = APIRouter()

@router.get("/image/{image_id}")
async def get_image(image_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(Config.CDN_URL + f"image/view/{image_id}")
    return Response(content=response.content, status_code=response.status_code)

@router.get("/video/{video_id}")
async def get_video(video_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(Config.CDN_URL + f"video/view/{video_id}")
    return Response(content=response.content, status_code=response.status_code)

@router.post('/xlsx')
async def get_xlsx(request: Request):
    try:
        data = await request.json()
        wb = create_xlsx(data)
        with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as tmp:
            temp_file_path = tmp.name
            wb.save(temp_file_path)
        return FileResponse(temp_file_path, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename="analysis.xlsx")
    except Exception as e:
        print(e)
        return {"error": "Invalid JSON format"}