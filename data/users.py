import dataclasses
from enum import StrEnum
from datetime import date


class Gender(StrEnum):
    Male = '[for="gender-radio-1"]'
    Female = '[for="gender-radio-2"]'
    Other = '[for="gender-radio-3"]'


class Hobbies(StrEnum):
    Sports = '[for="hobbies-checkbox-1"]'
    Reading = '[for="hobbies-checkbox-2"]'
    Music = '[for="hobbies-checkbox-3"]'


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
