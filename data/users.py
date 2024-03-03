import dataclasses
from enum import Enum
from datetime import date


class Gender(Enum):
    Male = 1
    Female = 2
    Other = 3


class Hobbies(Enum):
    Sports = 1
    Reading = 2
    Music = 3


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile_number: str
    birth_date: date
    subjects: str
    hobbies: Hobbies
    file_name: str
    current_address: str
    state: str
    city: str
    path: str
