from .database import supabase
from .schemas import OrderCreate

async def insert_order(data: OrderCreate):
    res = supabase.table("orders").insert(data.dict()).execute()
    return res.data[0]

async def list_orders():
    res = supabase.table("orders").select("*").execute()
    return res.data
