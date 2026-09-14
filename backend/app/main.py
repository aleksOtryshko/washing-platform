import json

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError

from .crud import insert_order
from .schemas import OrderCreate, OrderOut


app = FastAPI()


# Разрешённые фронтенды.
origins = [
    "https://aleksotryshko.github.io",
    "https://stiralka.site",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/orders", response_model=OrderOut)
async def create_order(request: Request):
    """
    Принимает заказ в двух форматах:

    1. application/json
       Обычный JSON для API-клиентов.

    2. text/plain
       JSON-строка внутри text/plain для браузерного фронтенда.

    text/plain используется на сайте для того, чтобы браузер мог
    отправить POST без предварительного CORS OPTIONS preflight.
    """

    content_type = (
        request.headers
        .get("content-type", "")
        .split(";", 1)[0]
        .strip()
        .lower()
    )

    try:
        if content_type == "application/json":
            payload = await request.json()

        elif content_type == "text/plain":
            raw_body = await request.body()

            payload = json.loads(
                raw_body.decode("utf-8")
            )

        else:
            raise HTTPException(
                status_code=415,
                detail=(
                    "Unsupported Content-Type. "
                    "Use application/json or text/plain."
                ),
            )

    except (json.JSONDecodeError, UnicodeDecodeError):
        raise HTTPException(
            status_code=400,
            detail="Invalid JSON body",
        )

    if not isinstance(payload, dict):
        raise HTTPException(
            status_code=422,
            detail="Request body must be a JSON object",
        )

    try:
        order = OrderCreate(
            **payload
        )

    except ValidationError as exc:
        raise HTTPException(
            status_code=422,
            detail=exc.errors(),
        )

    return await insert_order(
        order
    )
