from sqlalchemy import String, Column, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

from adapters.psql_database.base import BaseTable


class AccountsTable(BaseTable):
    email = Column(String, primary_key=True)
    password_hash = Column(String)
    confirmed = Column(Boolean)
    personal_data_id = Column(Integer, ForeignKey('PersonalDataTable.id'))
    personal_data = relationship('PersonalDataTable', uselist=False, backref='account')


class PersonalDataTable(BaseTable):
    id = Column(Integer, primary_key=True)
    account_email = Column(Integer, ForeignKey(AccountsTable.email))
    account = relationship(AccountsTable, uselist=False, backref='personal_data')
    first_name = Column(String)
    last_name = Column(String)
