from core.accounts.serializers import serialize_account
from core.cars.serializers import serialize_car
from core.trips.entities import Trip


def serialize_trip(trip: Trip) -> dict:
    return dict(
        trip_id=trip.trip_id,
        start_datetime=trip.start_datetime,
        estimated_end_date=trip.estimated_end_date,
        car=serialize_car(trip.car),
        customer=serialize_account(trip.customer),
        price_amount=trip.price_amount,
        paid=trip.paid,
        started=trip.started,
        ended=trip.ended,
        cancelled=trip.cancelled,
        real_end_date=trip.real_end_date,
    )
