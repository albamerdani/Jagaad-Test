from pydantic import BaseModel


class Stats(BaseModel):

    customerId: int
    type: str
    amount: int
    uuid: str

