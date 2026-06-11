from fastapi import APIRouter, UploadFile, File, Response
from app.services.face_detection import detect_faces, detect_faces_video
import tempfile
import os 
router = APIRouter()

@router.post("/detect")
async def detect(file: UploadFile = File(...)):
    image_bytes = await file.read()
    processed_image = detect_faces(image_bytes)
    return Response(content=processed_image, media_type="image/jpeg")
    
@router.post("/detect/video")
async def detect_video(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name
    output_path = tempfile.mktemp(suffix='.mp4')
    detect_faces_video(tmp_path, output_path)
    with open(output_path, 'rb') as f:
        video_bytes = f.read()
    os.remove(tmp_path)
    os.remove(output_path)
    return Response(content=video_bytes, media_type="video/mp4")
    