from dataclasses import dataclass


@dataclass
class Account:
    email: str
    personal_data: 'PersonalData'
    password_hash: str = None
    confirmed: bool = False


@dataclass
class PersonalData:
    first_name: str
    last_name: str
