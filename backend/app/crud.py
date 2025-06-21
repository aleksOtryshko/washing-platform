from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models, schemas

async def create_order(db: AsyncSession, data: schemas.OrderCreate):
    order = models.Order(**data.dict())
    db.add(order)
    await db.commit()
    await db.refresh(order)
    return order

async def create_master(db: AsyncSession, data: schemas.MasterCreate):
    master = models.Master(**data.dict())
    db.add(master)
    await db.commit()
    await db.refresh(master)
    return master

async def create_progress(db: AsyncSession, data: schemas.OrderProgressCreate):
    progress = models.OrderProgress(**data.dict())
    db.add(progress)
    await db.commit()
    await db.refresh(progress)
    return progress
