from sqlalchemy.orm import Session
from sqlalchemy import func

from app.model.message import Message as model
from app.db.database import SessionLocal


def process_message(db: Session, message: model):
    db_message = model(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


def get_stats(db: Session):
    query = (
        db.query(
            model.customer_id,
            model.type,
            func.count(model.id),
            func.sum(model.amount),
        )
        .where(model.date >= '2023-07-14 0:0' and model.date < '2023-07-19 0:0')
        .group_by(model.customer_id, model.type)
        .all()
    )
    stats = []
    for customer_id, message_type, count, total_amount in query:
        stats.append(
            {
                "customer_id": customer_id,
                "type": message_type,
                "count": count,
                "total_amount": total_amount,
            }
        )
    return stats


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
