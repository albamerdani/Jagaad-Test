from fastapi import APIRouter, Depends

from app.service.service import get_db
import app.model.message as msg
import app.service.service as service

router = APIRouter()


@router.post("/messages")
def process_message(message: msg.Message, db: Depends(get_db)):
    processed_message = service.process_message(db, message)
    return {"message": "Message processed successfully"}


@router.get("/stats")
def get_stats(db: Depends(get_db)):
    stats = service.get_stats(db)
    return {"stats": stats}
