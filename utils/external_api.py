import requests
from utils.config import Config

def upload_video(file_path: str) -> dict:
    with open(file_path, "rb") as f:
        response = requests.post(Config.CDN_URL + "video/upload/", files={"file": f})
    response.raise_for_status()
    return response.json()

def request_analysis(unique_id: str) -> dict:
    response = requests.post(Config.VIDEO_ANALYSIS_URL + unique_id)
    response.raise_for_status()
    return response.json()

def delete_video(video_id: str):
    response = requests.delete(Config.CDN_URL + f'video/delete/{video_id}')
    response.raise_for_status()
    return response.json()

def delete_image(image_id: str):
    response = requests.delete(Config.CDN_URL + f'image/delete/{image_id}')
    response.raise_for_status()
    return response.json()