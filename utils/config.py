from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    MONGODB_URI         = os.getenv('MONGODB_URI')
    CDN_URL             = os.getenv('CDN_URL')
    VIDEO_ANALYSIS_URL  = os.getenv('VIDEO_ANALYSIS_URL')