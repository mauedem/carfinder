from core.accounts.entities import Account
from core.cars.repos import ICarsRepo
from core.cars.schemas import CarSchema
from core.cars.serializers import serialize_car
from core.errors import CoreError, ErrorCodes


class CarsService:
    cars_repo: ICarsRepo
    
    def create_car(self, account: Account, car_data: dict) -> dict:
        validation_errors = CarSchema().validate(car_data)
        if validation_errors:
            raise CoreError(ErrorCodes.CAR_IS_NOT_A_VALID)
        
        car = self.cars_repo.create(account.email, car_data)
        
        return serialize_car(car)
    
    def get_car_by_id(self, car_id: int) -> dict:
        car = self.cars_repo.get_by_id(car_id)
        return serialize_car(car)
    
    def get_cars(self, limit: int = 30, offset: int = 0) -> list[dict]:
        cars = self.cars_repo.get_list(limit, offset)
        return [serialize_car(car) for car in cars]
