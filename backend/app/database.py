import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Берём URL из переменных окружения (Render/Supabase)
DATABASE_URL = os.getenv("DATABASE_URL")

# Синхронный движок
engine = create_engine(DATABASE_URL, echo=True, future=True)

# Обычная сессия
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)

Base = declarative_base()

# Зависимость для FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
