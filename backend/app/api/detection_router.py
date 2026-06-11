from fastapi import APIRouter
from fastapi import UploadFile, File, Response
from app.services.face_detection import detect_faces
router = APIRouter()

@router.post("/detect")
async def detect(file: UploadFile = File(...)):
    image_bytes = await file.read()
    processed_image = detect_faces(image_bytes)
    return Response(content=processed_image, media_type="image/jpeg")
    


     