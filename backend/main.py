from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import os

app = FastAPI()

class Order(BaseModel):
    name: str
    phone: str
    problem: str

@app.post("/submit")
def submit_order(order: Order):
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO orders (name, phone, problem, status) VALUES (%s, %s, %s, 'pending')",
        (order.name, order.phone, order.problem)
    )
    conn.commit()
    cur.close()
    conn.close()
    return {"ok": True}
