from pydantic import BaseModel
from typing import Optional, List
from datetime import date
from api.oportunidade_model import Oportunidade


class OportunidadeSchema(BaseModel):
    inclusao: Optional[date]
    titulo: str = 'Título'
    descricao: str = 'Descrição'
    status: Optional[bool] = 1
    idEmpresa: int = 1
    nomeEmpresa: str = 'Nome da Empresa'
    idPessoa: int = 1
    nomePessoa: str = 'Nome da Pessoa'
    updates: Optional[str]


class OportunidadeUpdateSchema(BaseModel):
    titulo: str = 'Título'
    descricao: str = 'Descrição'
    status: Optional[bool] = 1
    idEmpresa: int = 1
    nomeEmpresa: str = 'Nome da Empresa'
    idPessoa: int = 1
    nomePessoa: str = 'Nome da Pessoa'
    updates: Optional[str]


class OportunidadeByIdSchema(BaseModel):
    id: int


class OportunidadeByStatusSchema(BaseModel):
    status: bool


def serialize_oportunidade(oportunidade: Oportunidade):
    return {
        'id': oportunidade.id,
        'inclusao': oportunidade.inclusao,
        'titulo': oportunidade.titulo,
        'descricao': oportunidade.descricao,
        'status': oportunidade.status,
        'idEmpresa': oportunidade.idEmpresa,
        'nomeEmpresa': oportunidade.nomeEmpresa,
        'idPessoa': oportunidade.idPessoa,
        'nomePessoa': oportunidade.nomePessoa,
        'updates': oportunidade.updates
    }


def serialize_oportunidade_all(oportunidades: List[Oportunidade]):
    lista = []

    for oportunidade in oportunidades:
        lista.append(serialize_oportunidade(oportunidade))

    return lista
