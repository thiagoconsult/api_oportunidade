from api.db import engine
from sqlalchemy.orm import Session
from api.oportunidade_model import Oportunidade
from api.oportunidade_schema import (
    serialize_oportunidade,
    serialize_oportunidade_all,
    OportunidadeSchema,
    OportunidadeUpdateSchema,
    OportunidadeByIdSchema,
    OportunidadeByStatusSchema
)


#######################################################################
# POST - Serviço para Inclusão de Oportunidade
#######################################################################


def service_oportunidade_create(body: OportunidadeSchema):

    try:

        oportunidade = Oportunidade(
            inclusao=body.inclusao,
            titulo=body.titulo,
            descricao=body.descricao,
            status=body.status,
            idEmpresa=body.idEmpresa,
            nomeEmpresa=body.nomeEmpresa,
            idPessoa=body.idPessoa,
            nomePessoa=body.nomePessoa,
            updates=body.updates
        )

        with Session(engine) as session:
            session.add(oportunidade)
            session.commit()
            return serialize_oportunidade(oportunidade), 201
    except Exception as e:
        return {'err': f'Não foi possível realizar o cadastro {e.args}'}, 400


#######################################################################
# PUT - Serviço para Alteração de Oportunidade
#######################################################################


def service_oportunidade_update(query, body: OportunidadeUpdateSchema):

    with Session(engine) as session:
        oportunidade = session.query(Oportunidade).filter(
            Oportunidade.id == query.id).first()

        if not oportunidade:
            return {'err': 'Oportunidade não encontrada'}, 404

        try:
            oportunidade.titulo = body.titulo
            oportunidade.descricao = body.descricao
            oportunidade.status = body.status
            oportunidade.idEmpresa = body.idEmpresa
            oportunidade.nomeEmpresa = body.nomeEmpresa
            oportunidade.idPessoa = body.idPessoa
            oportunidade.nomePessoa = body.nomePessoa
            oportunidade.updates = body.updates

            session.commit()

            return serialize_oportunidade(oportunidade), 200
        except Exception as e:
            return {'err': f'Falha ao tentar atualizar oportunidade, detalhe: {e.args}'}, 400


#######################################################################
# DELETE - Serviço para Exclusão de Oportunidade
#######################################################################


def service_oportunidade_delete(query: OportunidadeByIdSchema):
    with Session(engine) as session:

        oportunidade = session.query(Oportunidade).filter(
            Oportunidade.id == query.id).first()

        if not oportunidade:
            return {'err': 'Nenhuma oportunidade encontrada'}, 404

        session.delete(oportunidade)
        session.commit()

        return {'Oportunidade excluída com sucesso': serialize_oportunidade(oportunidade)}


#######################################################################
# GET - Consulta Oportunidade por ID
#######################################################################


def service_oportunidade_get_by_id(query: OportunidadeByIdSchema):
    with Session(engine) as session:
        oportunidade = session.query(Oportunidade).filter(
            Oportunidade.id == query.id).first()

        if not oportunidade:
            return {'err': 'Oportunidade não encontrada'}, 404

        return serialize_oportunidade(oportunidade), 200

#######################################################################
# GET - Serviço para Consulta Lista de Oportunidades
#######################################################################


def service_oportunidade_get_all():
    with Session(engine) as session:

        oportunidades = session.query(Oportunidade).order_by(
            Oportunidade.status.desc()).all()

        if not oportunidades:
            return {'err': 'Nenhuma oportunidade encontrada'}, 404

        return serialize_oportunidade_all(oportunidades), 200


#######################################################################
# GET - Serviço para Consulta Quantidade de Oportunidades Por Status
#######################################################################


def service_oportunidade_get_count_by_status(query: OportunidadeByStatusSchema):
    with Session(engine) as session:
        oportunidades = session.query(Oportunidade).filter(
            Oportunidade.status == query.status)

        if not oportunidades:
            return {'err': 'Nenhuma oportunidade encontrada'}, 404

        quantidade = 0

        for oportunidade in oportunidades:
            quantidade += 1
            print(quantidade)

        return {'quantidade': quantidade}
