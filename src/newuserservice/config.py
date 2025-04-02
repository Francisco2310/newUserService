from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://usuario:senha@db:5432/meubanco"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASE_DIR = Path(__file__).resolve().parent
    