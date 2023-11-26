from sqlalchemy import create_engine, MetaData
from .config import settings

engine = create_engine(f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}')

meta = MetaData()

conn = engine.connect()




