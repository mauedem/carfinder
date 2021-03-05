from abc import ABC, abstractmethod

from core.cars.entities import Car


class ICarsRepo(ABC):
    
    @abstractmethod
    def create(self, account_email: str, car: dict) -> Car: ...
    
    @abstractmethod
    def get_by_id(self, car_id: int) -> Car: ...
    
    @abstractmethod
    def get_list(self, limit: int, offset: int) -> list[Car]: ...
    
    @abstractmethod
    def update(self, car_id: int, car_data: dict) -> None: ...
    
    @abstractmethod
    def delete(self, car_id: int) -> None: ...
