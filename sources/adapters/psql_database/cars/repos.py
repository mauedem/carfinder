from adapters.psql_database.base import BasePsqlRepo
from core.cars.entities import Car
from core.cars.repos import ICarsRepo


class PsqlCarsRepo(BasePsqlRepo, ICarsRepo):
    
    def create(self, account_email: str, car: dict) -> Car:
        pass

    def get_by_id(self, car_id: int) -> Car:
        pass

    def get_list(self, limit: int, offset: int) -> list[Car]:
        pass

    def update(self, car_id: int, car_data: dict) -> None:
        pass

    def delete(self, car_id: int) -> None:
        pass
