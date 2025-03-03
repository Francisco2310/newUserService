from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:francisco02699@localhost:5432/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASE_DIR = Path(__file__).resolve().parent
    