from fastapi import APIRouter, UploadFile, File
from uuid import uuid4

router = APIRouter(prefix="/api/files", tags=["files"])


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)) -> dict:
    return {"file_id": f"file_{uuid4().hex[:8]}", "filename": file.filename, "content_type": file.content_type}
