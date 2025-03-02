from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, DateTime
from extensions import db

class usuario(db.Model):
  __tablename__ = "usuarios"
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  nome: Mapped[str] = mapped_column(String(100), nullable=False)
  email: Mapped[str] = mapped_column(String(100), nullable=False)
  senha: Mapped[str] = mapped_column(String(100), nullable=False)
  criado_em: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
  def __init__(self, nome, email, senha):
    self.nome = nome
    self.email = email
    self.senha = senha 