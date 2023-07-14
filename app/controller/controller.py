from fastapi import APIRouter, Depends
from logging import log
from app.service.service import get_db
import app.model.message as msg
import app.service.service as service
import logging
from fastapi import FastAPI

#router = FastAPI()
router = APIRouter()

log = logging.getLogger("Jagaad Test Logs")


@router.post("/messages")
def process_message(message: msg.Message) -> msg.Message:
    db = Depends(get_db)
    processed_message = service.process_message(db, message)
    log.info("message: Message processed successfully")
    return message


@router.get("/")
def get_stats() -> list[msg.Message]:
    db = Depends(get_db)
    stats = service.get_stats(db)
    return stats



### Solution to use alembic as db framework for migrations


#from app.model.message import Stats as ModelMessage
#from app.db.schema import Stats as SchemaMessage
#from app import service


#@app.post("/stats/")
#async def create_stat(message: SchemaMessage):
#    message_id = await ModelMessage.create(**message.dict())
#    return {"message_id": message_id}


#@app.get("/stats/{id}", response_model=SchemaMessage)
#async def get_stat(id: int):
#    message = await ModelMessage.get(id)
#    return SchemaMessage(**message).dict()

