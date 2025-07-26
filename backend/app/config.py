import os
from dotenv import load_dotenv

# Загружаем локальный .env (если запускается локально)
load_dotenv()

# Если существует секретный файл от Render — загружаем его тоже
secret_env_path = "/etc/secrets/.env"
if os.path.exists(secret_env_path):
    load_dotenv(dotenv_path=secret_env_path)

# Теперь переменные будут доступны из окружения
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
