from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import engine, get_db, Base
from app import models, schemas, crud

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.post("/orders/", response_model=schemas.OrderCreate)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order)

@app.post("/masters/", response_model=schemas.MasterCreate)
def create_master(master: schemas.MasterCreate, db: Session = Depends(get_db)):
    return crud.create_master(db, master)

@app.post("/progress/", response_model=schemas.OrderProgressCreate)
def create_progress(progress: schemas.OrderProgressCreate, db: Session = Depends(get_db)):
    return crud.create_progress(db, progress)
