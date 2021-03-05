from abc import ABC, abstractmethod
from typing import Optional

from core.accounts.entities import Account


class IAccountsRepo(ABC):
    @abstractmethod
    def create(self, email: str, password_hash: str, first_name: str, last_name: str) -> Account: ...
    
    @abstractmethod
    def get_by_email(self, email: str) -> Optional[Account]: ...
    
    @abstractmethod
    def authorize(self, email: str, password_hash: str) -> Optional[Account]: ...
    
    @abstractmethod
    def update_email(self, old_email: str, new_email: str) -> None: ...
    
    @abstractmethod
    def update_personal_data(self, first_name: str, last_name: str) -> None: ...
    
    @abstractmethod
    def update_password(self, email: str, new_password_hash: str) -> None: ...
    
    @abstractmethod
    def delete(self, email: str) -> None: ...
