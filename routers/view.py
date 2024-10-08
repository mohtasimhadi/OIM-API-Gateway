from fastapi import APIRouter, Response
import httpx

router = APIRouter()

@router.get("/image/{image_id}")
async def get_image(image_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8000/image/view/{image_id}")
    return Response(content=response.content, status_code=response.status_code)

@router.get("/video/{video_id}")
async def get_video(video_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8000/video/view/{video_id}")
    return Response(content=response.content, status_code=response.status_code)
