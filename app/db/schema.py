from pydantic import BaseModel


class Message(BaseModel):
    customerId: int
    type: str
    amount: str
    uuid: str

