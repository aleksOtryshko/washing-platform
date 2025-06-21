from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class OrderStatusEnum(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"

class OrderCreate(BaseModel):
    phone_number: str
    name: str
    problem_description: str

class OrderProgressCreate(BaseModel):
    status: OrderStatusEnum
    order_id: int
    master_id: int
    comment: str

class MasterCreate(BaseModel):
    telegram_id: str
    name: str
