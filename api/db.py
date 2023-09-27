from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import create_engine
from os import path, makedirs

db_path = 'database'
db_url = f'sqlite:///{db_path}/db_oportunidade.sqlite3'

if not path.exists(db_path):
    makedirs(db_path)

engine = create_engine(db_url, echo=False, connect_args={
                       "check_same_thread": False})

if not database_exists(engine.url):
    create_database(engine.url)
