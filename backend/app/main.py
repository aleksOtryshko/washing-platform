from fastapi import FastAPI
from .schemas import OrderCreate, OrderOut
from .crud import insert_order

app = FastAPI()

@app.post("/api/orders", response_model=OrderOut)
async def create_order(order: OrderCreate):
    return await insert_order(order)
