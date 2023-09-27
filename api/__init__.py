from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS
from api.routes import api
from api import db, oportunidade_model


info = Info(title='Microserviço de Oportunidade', version='1.0.1',
            description='Gestão do Cadastro de Oportunidade')

app = OpenAPI(__name__, info=info)

CORS(app)

app.register_api(api)
