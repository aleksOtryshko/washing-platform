from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Enum
from sqlalchemy.sql import func
from .database import Base
import enum

class OrderStatus(enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    phone_number = Column(String, nullable=False)
    name = Column(String, nullable=False)
    problem_description = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Master(Base):
    __tablename__ = "masters"
    id = Column(Integer, primary_key=True)
    telegram_id = Column(String, unique=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class OrderProgress(Base):
    __tablename__ = "order_progress"
    id = Column(Integer, primary_key=True)
    status = Column(Enum(OrderStatus), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    master_id = Column(Integer, ForeignKey("masters.id"), nullable=False)
    comment = Column(Text)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
