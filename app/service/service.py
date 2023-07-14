from sqlalchemy.orm import Session
from sqlalchemy import func

from app import model
from app.db.database import SessionLocal


def process_message(db: Session, message: model.Message):
    db_message = model.Message(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


def get_stats(db: Session):
    query = (
        db.query(
            model.Message.customerId,
            model.Message.type,
            func.count(model.Message.id),
            func.sum(model.Message.amount),
        )
        .group_by(model.Message.customerId, model.Message.type)
        .all()
    )
    stats = []
    for customerId, messageType, count, totalAmount in query:
        stats.append(
            {
                "customerId": customerId,
                "type": messageType,
                "count": count,
                "totalAmount": totalAmount,
            }
        )
    return stats


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
