from typing import Any
from sqlalchemy import String, Integer, Boolean, Date
from datetime import date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from api.db import engine


class Base(DeclarativeBase):
    pass


class Oportunidade(Base):
    __tablename__ = 'oportunidade'

    id: Mapped[int] = mapped_column(primary_key=True)
    inclusao: Mapped[date] = mapped_column(Date, default=date.today)
    titulo: Mapped[str] = mapped_column(String(100))
    descricao: Mapped[str] = mapped_column(String(255))
    status: Mapped[bool] = mapped_column(Boolean, default=1)
    idEmpresa: Mapped[int] = mapped_column(Integer)
    nomeEmpresa: Mapped[str] = mapped_column(String(50))
    idPessoa: Mapped[int] = mapped_column(Integer)
    nomePessoa: Mapped[str] = mapped_column(String(100))
    updates: Mapped[str] = mapped_column(String(5000))

    def __init__(self, inclusao: date, titulo: str, descricao: str, status: bool, idEmpresa: int, nomeEmpresa: str, idPessoa: int, nomePessoa: str, updates: str):
        self.inclusao = inclusao
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.idEmpresa = idEmpresa
        self.nomeEmpresa = nomeEmpresa
        self.idPessoa = idPessoa
        self.nomePessoa = nomePessoa
        self.updates = updates


Base.metadata.create_all(engine)
