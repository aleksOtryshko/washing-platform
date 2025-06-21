from sqlalchemy.orm import Session
from . import models, schemas

def create_order(db: Session, data: schemas.OrderCreate):
    order = models.Order(**data.dict())
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def create_master(db: Session, data: schemas.MasterCreate):
    master = models.Master(**data.dict())
    db.add(master)
    db.commit()
    db.refresh(master)
    return master

def create_progress(db: Session, data: schemas.OrderProgressCreate):
    progress = models.OrderProgress(**data.dict())
    db.add(progress)
    db.commit()
    db.refresh(progress)
    return progress
