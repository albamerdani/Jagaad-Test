from app.db import db, sqlalchemy

messages = sqlalchemy.Table(
    "message",
    sqlalchemy.Column("customerId", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("type", sqlalchemy.String),
    sqlalchemy.Column("amount", sqlalchemy.DOUBLE),
    sqlalchemy.Column("uuid", sqlalchemy.UUID),
)


class Message:
    @classmethod
    async def get(cls, id):
        query = messages.select().where(messages.c.id == id)
        message = await db.fetch_one(query)
        return message

    @classmethod
    async def create(cls, **message):
        query = messages.insert().values(**message)
        message_id = await db.execute(query)
        return message_id

