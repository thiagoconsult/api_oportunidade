from flask_openapi3 import APIBlueprint, Tag
from flask import redirect
from api.oportunidade_schema import (
    OportunidadeSchema,
    OportunidadeUpdateSchema,
    OportunidadeByIdSchema,
    OportunidadeByStatusSchema
)
from api.oportunidade_services import (
    service_oportunidade_create,
    service_oportunidade_update,
    service_oportunidade_delete,
    service_oportunidade_get_all,
    service_oportunidade_get_by_id,
    service_oportunidade_get_count_by_status

)

tag_oportunidade = Tag(name='Cadastro de Oportunidade',
                       description='Inclusão, Alteração, Consulta e Exclusão de oportunidade')

api = APIBlueprint(
    'OPORTUNIDADE',
    __name__,
    abp_tags=[tag_oportunidade]
)


#######################################################################
# Redirecionamento para a documentação Swagger
#######################################################################


@api.route('/')
def index():
    return redirect('/openapi/swagger')


#######################################################################
# POST - Inclusão de Oportunidade
#######################################################################


@api.post(
    '/oportunidade',
    summary='Inclusão de Oportunidade',
    description='Método para inclusão de oportunidades pelo front-end'
)
def oportunidade_create(body: OportunidadeSchema):
    return service_oportunidade_create(body)


#######################################################################
# PUT - Alteração de Oportunidade
#######################################################################


@api.put(
    '/oportunidade',
    summary='Alteração de Oportunidade',
    description='Método para alteração de oportunidades pelo front-end'
)
def oportunidade_update(query: OportunidadeByIdSchema, body: OportunidadeUpdateSchema):
    return service_oportunidade_update(query, body)


#######################################################################
# DELETE - Exclusão de Oportunidade
#######################################################################


@api.delete(
    '/oportunidade',
    summary='Exclusão de Oportunidade',
    description='Método para exclusão de oportunidades pelo front-end'
)
def oportunidade_delete(query: OportunidadeByIdSchema):
    return service_oportunidade_delete(query)


#######################################################################
# GET - Consulta Oportunidade por ID
#######################################################################


@api.get(
    '/oportunidade/id',
    summary='Consulta Oportunidade por ID',
    description='Método para consulta de oportunidades por ID pelo front-end'
)
def oportunidade_get_by_id(query: OportunidadeByIdSchema):
    return service_oportunidade_get_by_id(query)


#######################################################################
# GET - Consulta Lista de Oportunidades
#######################################################################


@api.get(
    '/oportunidade/all',
    summary='Consulta Lista de Oportunidades',
    description='Método para consulta lista de oportunidades pelo front-end'
)
def oportunidade_get_all():
    return service_oportunidade_get_all()


#######################################################################
# GET - Consulta Quantidade de Oportunidades Por Status
#######################################################################


@api.get(
    '/oportunidade/count/status',
    summary='Consulta Quantidade de Oportunidades Por Status',
    description='Método para consulta quantidade de oportunidades por status pelo front-end'
)
def oportunidade_get_count_by_status(query: OportunidadeByStatusSchema):
    return service_oportunidade_get_count_by_status(query)
