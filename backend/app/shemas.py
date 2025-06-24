from pydantic import BaseModel

class OrderCreate(BaseModel):
    phone_number: str
    name: str
    problem_description: str

class OrderOut(OrderCreate):
    id: int
    status: str
    created_at: str
