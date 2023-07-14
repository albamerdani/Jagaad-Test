from app.db.database import sqlalchemy, engine, SessionLocal
from sqlalchemy import Column, Integer, String, Double, UUID, DateTime
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel


Base = declarative_base()


# Define the Message model for the statistics table
class Message(Base):
    __tablename__ = "stats"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer)
    type = Column(String)
    amount = Column(String)
    uuid = Column(String)
    date = Column(DateTime)


# Request body model based on the JSON schema
class MessageType(BaseModel):
    __tablename__ = "messageType_stats"
    message_type = Column(String, primary_key=True, index=True)   #str
    message_count = Column(Integer)  #int
    total_amount = Column(Double) #float


# Request body model based on the JSON schema
class MessageUuid(BaseModel):
    __tablename__ = "messageUuid_stats"
    message_uuid = Column(String, primary_key=True, index=True)   #str
    message_type = Column(String)   #str
    customer_id = Column(Integer)  #int
    total_amount = Column(Double) #float


# Request body model based on the JSON schema
class CustomerId(BaseModel):
    __tablename__ = "customerId_stats"
    message_uuid = Column(String, primary_key=True, index=True)   #str
    customer_id = Column(Integer)  #int
    message_type = Column(String)   #str
    amount = Column(Double) #float

# Create the table if it doesn't exist
Base.metadata.create_all(bind=engine)


### Solution to use alembic as db framework for migrations


#
# class Stats(BaseModel):
#
#     customer_id: int
#     type: str
#     amount: int
#     uuid: str
#     date: date
#
#
# stats = sqlalchemy.Table(
#     "stats",
#     sqlalchemy.Column("customer_id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("type", sqlalchemy.String),
#     sqlalchemy.Column("amount", sqlalchemy.DOUBLE),
#     sqlalchemy.Column("uuid", sqlalchemy.UUID),
#     sqlalchemy.Column("date", sqlalchemy.DateTime),
# )
#
#
# class Stats(Base):
#     __tablename__ = "stats"
#
#     customerId = Column(Integer, primary_key=True)
#     type = Column(String)
#     amount = Column(Double)
#     uuid = Column(UUID)
#     date = Column(DateTime)
#
#     Base.metadata.create_all(engine)
#
#     @classmethod
#     async def get(cls, id):
#         query = stats.select().where(stats.c.id == id)
#         message = await engine.fetch_one(query)
#         return message
#
#     @classmethod
#     async def create(cls, **message):
#         query = stats.insert().values(**message)
#         message_id = await engine.execute(query)
#         return message_id

