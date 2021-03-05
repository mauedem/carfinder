from dataclasses import dataclass
from datetime import datetime

from core.accounts.entities import Account


@dataclass
class Car:
    car_id: int
    model: str
    category: str
    year_of_manufacture: int
    hoster: Account
    tags: list['Tag']
    reviews: list['Review']
    extras: list['Extra']
    description: str
    features: list['Tag']
    guidelines: str
    faqs: dict[str, str]
    current_geotag: str
    price: float


@dataclass
class Tag:
    icon: str
    name: str


@dataclass
class Review:
    account: Account
    datetime_of_create: datetime
    evaluation: int
    comment: str


@dataclass
class Extra:
    name: str
    description: str
    price: float
    
