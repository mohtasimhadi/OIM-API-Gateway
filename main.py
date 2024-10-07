from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import upload, analysis

app = FastAPI()

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(analysis.router, prefix="/data", tags=["Analysis"])

if __name__ == "__main__":
    import uvicorn
    print("Registered routers:", app.routes)
    uvicorn.run(app, host="0.0.0.0", port=8080)