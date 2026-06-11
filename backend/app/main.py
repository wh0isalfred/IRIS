from fastapi import FastAPI
from app.api.detection_router import router as detection_router

app = FastAPI()

app.include_router(detection_router)
