from fastapi import APIRouter, Response
import httpx
from utils.config import Config

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
