from adapters.psql_database.base import BasePsqlRepo
from core.trips.entities import Trip
from core.trips.repos import ITripsRepo


class PsqlTripsRepo(BasePsqlRepo, ITripsRepo):
    
    def create(self, customer_email: str, trip_data: dict) -> Trip:
        pass

    def set_paid(self, trip_id: int) -> None:
        pass

    def set_started(self, trip_id: int) -> None:
        pass

    def set_ended(self, trip_id: int) -> None:
        pass

    def set_cancelled(self, trip_id: int) -> None:
        pass
