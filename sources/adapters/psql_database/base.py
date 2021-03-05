from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


class BasePsqlRepo:
    def __init__(self, session: Session):
        self.session = session


BaseTable = declarative_base()

