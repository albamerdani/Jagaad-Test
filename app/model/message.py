from app.db.database import db, sqlalchemy, engine
from sqlalchemy import Column, Integer, String, Double, UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()

stats = sqlalchemy.Table(
    "stats",
    sqlalchemy.Column("customerId", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("type", sqlalchemy.String),
    sqlalchemy.Column("amount", sqlalchemy.DOUBLE),
    sqlalchemy.Column("uuid", sqlalchemy.UUID),
)


class Stats(Base):
    __tablename__ = "stats"

    customerId = Column(Integer, primary_key=True)
    type = Column(String)
    amount = Column(Double)
    uuid = Column(UUID)

    Base.metadata.create_all(engine)

    @classmethod
    async def get(cls, id):
        query = stats.select().where(stats.c.id == id)
        message = await db.fetch_one(query)
        return message

    @classmethod
    async def create(cls, **message):
        query = stats.insert().values(**message)
        message_id = await db.execute(query)
        return message_id

