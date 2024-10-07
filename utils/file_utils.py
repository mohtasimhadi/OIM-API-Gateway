import os
import shutil
from fastapi import UploadFile

UPLOAD_DIRECTORY = "./uploads"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

def save_upload_file(upload_file: UploadFile) -> str:
    """Save an uploaded file to the upload directory and return its path."""
    file_path = os.path.join(UPLOAD_DIRECTORY, upload_file.filename)
    with open(file_path, "wb") as f:
        shutil.copyfileobj(upload_file.file, f)
    return file_path

def remove_file(file_path: str):
    """Remove the file at the given file path."""
    if os.path.exists(file_path):
        os.remove(file_path)
