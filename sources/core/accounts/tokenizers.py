from abc import ABC, abstractmethod
from typing import Optional


class IPasswordTokenizer(ABC):
    @abstractmethod
    def encode(self, password: str) -> str: ...


class IAccessTokenizer(ABC):
    @abstractmethod
    def encode(self, account_data: dict) -> str: ...
    
    @abstractmethod
    def decode(self, token: str) -> Optional[dict]: ...
