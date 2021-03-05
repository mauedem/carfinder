from abc import ABC, abstractmethod

from core.trips.entities import Trip


class ITripsRepo(ABC):
    
    @abstractmethod
    def create(self, customer_email: str, trip_data: dict) -> Trip: ...
    
    @abstractmethod
    def set_paid(self, trip_id: int) -> None: ...
    
    @abstractmethod
    def set_started(self, trip_id: int) -> None: ...
    
    @abstractmethod
    def set_ended(self, trip_id: int) -> None: ...
    
    @abstractmethod
    def set_cancelled(self, trip_id: int) -> None: ...
