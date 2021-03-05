from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from boot import settings


db_engine = create_engine(settings.DB_URL)

PsqlSession = sessionmaker(bind=db_engine, autoflush=True, autocommit=True)
