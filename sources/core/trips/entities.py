from dataclasses import dataclass
from datetime import datetime

from core.accounts.entities import Account
from core.cars.entities import Car


@dataclass
class Trip:
    trip_id: int
    start_datetime: datetime
    estimated_end_date: datetime
    car: Car
    customer: Account
    price_amount: float
    paid: bool = False
    started: bool = False
    ended: bool = False
    cancelled: bool = False
    real_end_date: datetime = None
