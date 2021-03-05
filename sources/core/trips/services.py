from core.accounts.entities import Account
from core.errors import ErrorCodes, CoreError
from core.trips.repos import ITripsRepo
from core.trips.schemas import TripSchema
from core.trips.serializers import serialize_trip


class TripsService:
    trips_repo: ITripsRepo
    def checkout(self, account: Account, trip_data: dict):
        validation_errors = TripSchema().validate(trip_data)
        
        if validation_errors:
            raise CoreError(ErrorCodes.TRIP_IS_NOT_A_VALID)
        
        trip = self.trips_repo.create(account.email, trip_data)
        
        return serialize_trip(trip)
