from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .schemas import OrderCreate, OrderOut
from .crud import insert_order

app = FastAPI()

# 1) Разрешённый фронт
origins = [
    "https://aleksotryshko.github.io",
    "https:/stiralka.site",
    # если будете тестить локально, можно раскомментировать:
    # "http://localhost:5500",
    # "http://127.0.0.1:5500",
]

# 2) Подключаем CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # кому можно шортить запросы
    Allow_credentials=True,      # если нужны куки/авторизация
    allow_methods=["*"],         # все HTTP-методы
    allow_headers=["*"],         # все заголовки
)

@app.post("/api/orders", response_model=OrderOut)
async def create_order(order: OrderCreate):
    """
    Принимаем JSON с полями:
      - name: str
      - phone: str
      - problem: str
    Сохраняем через insert_order и возвращаем OrderOut.
    """
    return await insert_order(order)

'''
from fastapi import FastAPI
from .schemas import OrderCreate, OrderOut
from .crud import insert_order

app = FastAPI()

@app.post("/api/orders", response_model=OrderOut)
async def create_order(order: OrderCreate):
    return await insert_order(order)
'''
