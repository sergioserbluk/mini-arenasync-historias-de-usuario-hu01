from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


class Config:
    SECRET_KEY = "mini-arenasync-dev"
    RESULTADOS_PATH = BASE_DIR / "data" / "resultados.json"
