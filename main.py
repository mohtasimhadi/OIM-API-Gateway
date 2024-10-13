import socket
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import upload, analysis, view, delete

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(analysis.router, prefix="/data", tags=["Analysis"])
app.include_router(view.router, prefix="/view", tags=["Analysis"])
app.include_router(delete.router, prefix='/delete', tags=["Delete"])

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

if __name__ == "__main__":
    import uvicorn
    local_ip = get_local_ip()
    print(f"\033[92mINFO:  \t\033[0m  App is accessible at: \033[94mhttp://{local_ip}:8080\033[0m")
    uvicorn.run(app, host="0.0.0.0", port=8080)