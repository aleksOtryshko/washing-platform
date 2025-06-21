from fastapi import FastAPI, Depends
from . import models, schemas, crud
from .database import engine, get_db, Base
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post("/orders/")
async def create_order(order: schemas.OrderCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_order(db, order)

@app.post("/masters/")
async def create_master(master: schemas.MasterCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_master(db, master)

@app.post("/progress/")
async def create_progress(progress: schemas.OrderProgressCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_progress(db, progress)
