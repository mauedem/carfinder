from inject import Binder
from sqlalchemy.orm import Session

from adapters.psql_database.config import PsqlSession


class SiteContainer:
    def __call__(self, binder: Binder):
        binder.bind(Session, PsqlSession())
        
        binder.bind()
    