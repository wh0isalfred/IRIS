from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.detection_router import router as detection_router

app = FastAPI()

# Middleware first — it wraps everything below
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Then routes
app.include_router(detection_router)