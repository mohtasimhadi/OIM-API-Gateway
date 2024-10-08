import requests

EXTERNAL_API_URL = "http://localhost:8000/video/upload"

def send_file_to_external_api(file_path: str) -> dict:
    """Send a file to the external API and return the response data."""
    with open(file_path, "rb") as f:
        response = requests.post(EXTERNAL_API_URL, files={"file": f})
    response.raise_for_status()
    return response.json()

def request_analysis(unique_id: str) -> dict:
    """Request analysis from the external API using the unique ID."""
    response = requests.post(f"http://localhost:5000/{unique_id}")
    response.raise_for_status()
    return response.json()